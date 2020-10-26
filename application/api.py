from flask import Flask, request, render_template
import os
import json
from modules import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_file():

    if request.method == 'GET':
        return render_template("upload.html")

    if request.method == "POST":
        f = request.files['file']
        f_name = f.filename

        pid = os.fork()
        if pid > 0: 

            print("\nIn parent process",os.getpid()) 
            # Wait for the completion of child process and get its pid and exit status indication using os.wait() method 
            info = os.waitpid(pid, 0) 
 
            if os.WIFEXITED(info[1]) : 
                code = os.WEXITSTATUS(info[1]) 
                print("Child's exit code:", code) 
                status= 200
                response_type = 'application/json'
                result= {"Status":"Success", "Response": "Task Completed","Child's exit code":code}
                response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)            
                return response

        else : 
            print("In child process:", os.getpid()) 
            
            manipulate_process.start_process("PROC_1")
            
            print("Child exiting..") 
        
            os._exit(os.EX_OK) 
        
        # if f_name!='':
        #     f_path = './upload/'+f_name
        #     f.save(f_path)
        #     print('file uploaded successfully')
            
        #     start_process.start_process()
        #     status= 200
        #     response_type = 'application/json'
        #     result= {"Status":"Success", "Response":f_name+" is successfully stored"}
        #     response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)            
        #     return response
    
        # else:
        #     status= 400
        #     response_type = 'application/json'
        #     result= {"Status":"Failed", "Response":"No file found!. Please upload any file."}
        #     response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
        #     return response


@app.route("/stop", methods=['GET', 'POST'])
def stop():

    if request.method == "GET":
        try:
            verdict = manipulate_process.stop_process("PROC_1")
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
            verdict = manipulate_process.pause_process("PROC_1")
            return render_template("upload.html")
            # status= 200
            # response_type = 'application/json'
            # result= {"Status":"Success", "Response": verdict}
            # response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            # return response

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
            verdict = manipulate_process.resume_process("PROC_1")
            return render_template("upload.html")
            # status= 200
            # response_type = 'application/json'
            # result= {"Status":"Success", "Response": verdict}
            # response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            # return response

        except Exception as e:
            status= 400
            response_type = 'application/json'
            result= {"Status":"Failed", "Response":str(e)}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=6850, debug=True)