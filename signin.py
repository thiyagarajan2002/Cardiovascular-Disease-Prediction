from flask import Flask
from flask import render_template,redirect,request

app=Flask(__name__)
    

#ok
@app.route('/',methods = ['POST', 'GET'])  
def Sign_in():
    return render_template('Sign_in.html',status=" ") 

#ok
@app.route('/login',methods = ['POST', 'GET'])  
def login():
    email=request.form['email']  
    password=request.form['password']
    result=ps.login(email,password)
    if result:
        return render_template('Sign_in.html',status="OK")
    else:
        return render_template('Sign_in.html',status="Invalid Details")

if __name__ =='__main__':  
    app.run(debug = True)  
