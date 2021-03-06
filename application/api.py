from flask import Flask, request, render_template
import os
import json
import logging
from modules.manipulate_process import *

app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route("/", methods=['GET', 'POST'])
def upload_file():

    if request.method == 'GET':
        return render_template("upload.html")

    if request.method == "POST":
        # f = request.files['file']
        # f_name = f.filename
        # if f_name!='':
        #     f_path = './upload/'+f_name
        #     f.save(f_path)
        #     print('file uploaded successfully')

        r, w = os.pipe() 
        pid = os.fork()
        
        if pid: 

            print("\nIn parent process",os.getpid()) 
            # Wait for the completion of child process and get its pid and exit status indication using os.wait() method 
            info = os.waitpid(pid, 0) 
            
            if os.WIFEXITED(info[1]) :
                os.close(w) 
                r = os.fdopen(r) 
                f_result = r.read() 
                
                if f_result:
                    code = os.WEXITSTATUS(info[1]) 
                    print("Child's exit code:", code) 
                    status= 400
                    response_type = 'application/json'
                    result= {"Status":"Failed", "Response": f_result,"Child's exit code":code}
                    response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)            
                    return response
                
                else:
                    code = os.WEXITSTATUS(info[1])
                    print("Child's exit code:", code) 
                    status= 200
                    response_type = 'application/json'
                    result= {"Status":"Success", "Response": "Task Completed","Child's exit code":code}
                    response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)            
                    return response

        else : 
        
            print("In child process:", os.getpid()) 

            os.close(r)
            w = os.fdopen(w, 'w')

            res_ins = start_process("PROC_1")
                        
            w.write(str(res_ins))
            w.close()
        
            print("Child exiting..") 
        
            os._exit(os.EX_OK)
                    
@app.route("/stop", methods=['GET', 'POST'])
def stop():

    if request.method == "GET":
        try:
            verdict =  stop_process("PROC_1")
            status= 200
            response_type = 'application/json'
            result= {"Status":"Success", "Response": verdict}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

        except Exception as e:
            status= 400
            response_type = 'application/json'
            result= {"Status":"Failed", "Response":str(e)}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

@app.route("/pause", methods=['GET', 'POST'])
def paused():

    if request.method == "GET":
        try:
            verdict =  pause_process("PROC_1")
            # return render_template("upload.html")
            # status= 200
            # response_type = 'application/json'
            # result= {"Status":"Success", "Response": verdict}
            # response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            # return response
            return ('', 204)            

        except Exception as e:
            status= 400
            response_type = 'application/json'
            result= {"Status":"Failed", "Response":str(e)}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

@app.route("/resume", methods=['GET', 'POST'])
def resume():

    if request.method == "GET":
        try:
            verdict =  resume_process("PROC_1")
            # return render_template("upload.html")
            # status= 200
            # response_type = 'application/json'
            # result= {"Status":"Success", "Response": verdict}
            # response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            # return response
            return ('', 204)

        except Exception as e:
            status= 400
            response_type = 'application/json'
            result= {"Status":"Failed", "Response":str(e)}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

if __name__ == "__main__":
    #app.run(debug=True,port=7001)
    app.run(port=7001, debug=True)