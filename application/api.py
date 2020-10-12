from flask import Flask, request, render_template
import os
import json
#import re
#import send_mail

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
flag = 0

@app.route("/", methods=['GET', 'POST'])

def upload_file():
    global flag
    if request.method == 'GET':
        return render_template("upload.html")

    if request.method == "POST":
        f = request.files['file']
        f_name = f.filename
        if f_name!='':
            flag = 1
            f_path = './upload/'+f_name
            f.save(f_path)
            print('file uploaded successfully')
            
            status= 200
            response_type = 'application/json'
            result= {"Status":"Success", "Response":f_name+" is successfully stored"}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            flag = 0
            return response
        
        else:
            status= 400
            response_type = 'application/json'
            result= {"Status":"Failed", "Response":"No file found!. Please upload any file."}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

@app.route("/stop", methods=['GET', 'POST'])
def stop_process():
    global flag
    if request.method == "GET":
        if flag==1:
            status= 200
            response_type = 'application/json'
            result= {"Status":"Success", "Response":"Processing stopped"}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            flag = 0
            return response
        else:
            status= 200
            response_type = 'application/json'
            result= {"Status":"Failed", "Response":"No process to stop"}
            response = app.response_class(response=json.dumps(result), status=status, mimetype=response_type)
            return response

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=6850, debug=True)