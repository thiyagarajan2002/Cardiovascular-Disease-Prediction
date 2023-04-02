from flask import Flask
from flask import render_template,redirect,request,url_for

app=Flask(__name__)
    

@app.route('/',methods = ['POST', 'GET'])  
def Sign_up():  
    return render_template('Sign_up.html',status=" ")

#ok
@app.route('/Sign up status',methods = ['POST', 'GET'])  
def Sign_up_status():
    name=request.form['name']
    phone_number=request.form['phone_number']
    email=request.form['email']
    password=request.form['password']
    #result=ps.sign_up(name,email,phone_number,password)
    result=False
    if result:
        return redirect(url_for('Sign_in'))
    else:
        return render_template('Sign_up.html',status="Invalid Details")
   
#ok
@app.route('/Sign_in',methods = ['POST', 'GET'])  
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
