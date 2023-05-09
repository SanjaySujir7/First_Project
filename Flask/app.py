
from flask import Flask, redirect, render_template
from flask import request
import sqlite3




app = Flask(__name__)


@app.route("/error")
def Error(reason):
    return render_template("error.html",error_name = reason)


@app.route('/login-data',methods = ['POST'])
def Login_Data_Process():
    Name_Email = request.form["name_email"]
    Password = request.form['password']
    found = False
    
    print(Name_Email,Password)
    
    if Password and Name_Email:
        if len(Password) > 6 and Name_Email.isdigit() != True:
            Conn = sqlite3.connect("user.db")
            c = Conn.cursor()
            
            if "@" in Name_Email and ".com" in Name_Email:
                c.execute("SELECT * FROM user_info WHERE Email = ?",(Name_Email,))
                data = c.fetchall()
                if data:
                    if data[0][2] == Name_Email:
                        found = True
                        
                    else:
                        found = False
                
                else:
                    found = False
                
            else:
                c.execute("SELECT * FROM user_info WHERE Name = ?",(Name_Email,))
                data = c.fetchall()
                
                if data:
                    if data[0][0] == Name_Email:
                        found = True
                     
                    else:
                        found = False
                           
                    
                else:
                    found = False
                    
            c.execute("SELECT * FROM user_info WHERE Password = ?",(Password,))
            data = c.fetchall()

            if data:
                if data[0][3] == Password:
                    Pass_Found = True
                    
                else:
                    Pass_Found = False
                
            else:
                Pass_Found = False
            
            
            if found and Pass_Found:
                return " data submited and it is valid"
            
            else:
                return Error("The data is not found ! please check whether you have account or not. \nif you dont have account create one")
            
    else:
        return Error("Data is not valid")
                    
                
    
    return "data Submited"
                
        
            
@app.route('/login')
def Login ():
    return render_template('Login.html')

@app.route('/sign-up')
def Sign_Up():
    return render_template('index.html')

@app.route('/sign-up-data',methods=['POST'])
def Get_Data():
    
    Name = request.form['Name']
    Last_Name = request.form['Last']
    Email = request.form['Email']
    Password = request.form['Password']
    Language = request.form['Lang']
    Status= request.form['Stat']
    Radio = request.form['topic']
    
    if Name and Last_Name and Email and Password and Language and Status and Radio :
        password = False
        email = False
        
        if len(Password) > 6:
            password = True
            
        if '@' in Email and '.com' in Email:
            email = True
            
        if password and email :
            
            Return_boolean = True
            
            conn = sqlite3.connect('user.db')
            
            c = conn.cursor()
            
            c.execute("CREATE TABLE IF NOT EXISTS user_info (Name , Last_name , Email , Password , Language , Status , Radio)")
            
            conn.commit()
            
            c.execute(""" INSERT INTO user_info (Name , Last_name , Email , Password , Language , Status , Radio) 
                        VALUES ( :Name , :Last_name , :Email , :Password , :Language , :Status , :Radio)
                        
                        """,{ 'Name' :Name ,'Last_name' :Last_Name, 'Email' :Email, 'Password' :Password, 'Language' : Language, 'Status' :Status, 'Radio' :Radio})
            
            conn.commit()
            conn.close()
                
    
        else:
            Return_boolean = False
            
        if Return_boolean:
            return redirect('/login')
        else:
            return Error("The data is invalid")
            
    else :
        return Error('The data is invalid')

if __name__ == '__main__':
    app.run(
        debug=True,
        host='127.0.0.1',
        port=5001
            
            )
 