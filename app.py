from flask import Flask
from flask import render_template,redirect,request,url_for
import pandas as pd
import sys
import numpy as np
import pickle
import process as ps
app=Flask(__name__)
    
model=pickle.load(open('model.pkl','rb'))  

#ok  
@app.route('/')  
def Main():  
    return render_template('Home.html') 

#ok
@app.route('/Sign_up',methods = ['POST', 'GET'])  
def Sign_up():  
    return render_template('Sign_up.html',status=" ")

#ok
@app.route('/Sign_up_status',methods = ['POST', 'GET'])  
def Sign_up_status():
    name=request.form['name']
    phone_number=request.form['phone_number']
    email=request.form['email']
    password=request.form['password']
    result=ps.sign_up(name,phone_number,email,password)
    #result=False
    if result:
        return redirect(url_for('Sign_in'))
    else:
        return render_template('Sign_up.html',status="Invalid Details")


#ok
@app.route('/Sign_in',methods = ['POST', 'GET'])  
def Sign_in():
    return render_template('Log_in.html',status=" ") 

#ok
@app.route('/Home',methods = ['POST', 'GET'])  
def Home():
    email=request.form['email']  
    password=request.form['password']
    result=ps.login(email,password)
    user_id=ps.get_id(email)
    if result:
        return render_template('Disease_prediction.html',user_id=user_id,result=" ")
    else:
        return render_template('Log_in.html',status="Invalid Details") 


#ok
@app.route('/Result', methods = ['POST', 'GET'])  
def Result():
    if request.method=='POST':
        user_id=request.form["user_id"]
        age=request.form["age"]
        serum_cholestoral=request.form["serum_cholestoral"]
        chest=request.form["chest"]	
        resting_blood_pressure=request.form["resting_blood_pressure"]
        maximum_heart_rate_achieved=request.form["maximum_heart_rate_achieved"]
        oldpeak=request.form["oldpeak"]
        thal=request.form["thal"]
        sex=request.form["gender"]
        fasting_blood_sugar=request.form['fasting_blood_sugar']	
        resting_electrocardiographic_results=request.form['resting_electrocardiographic_results']		
        exercise_induced_angina=request.form['exercise_induced_angina']
        slope=request.form['slope']
        number_of_major_vessels=request.form['number_of_major_vessels']
        lst=list()
        lst.append((age))
        lst.append((sex))
        lst.append((chest))
        lst.append((resting_blood_pressure))
        lst.append((serum_cholestoral))
        lst.append((fasting_blood_sugar))
        lst.append((resting_electrocardiographic_results))
        lst.append((maximum_heart_rate_achieved))
        lst.append((exercise_induced_angina))
        lst.append((oldpeak))
        lst.append((slope))
        lst.append((number_of_major_vessels))
        lst.append((thal))
        ans=model.predict([np.array(lst,dtype='int64')])
        result=int(ans[0])
        status=ps.store(user_id,result)
        if status:
            return render_template("Disease_prediction.html",result=result)

"""
#ok
@app.route('/Log_out')  
def Log_out():  
     return redirect(url_for('/'))

#ok
@app.route('/Back')  
def Back():  
     return redirect(url_for('Home'))

"""
if __name__ =='__main__':  
    app.run(debug = True)  
