
from flask import Flask, redirect, render_template,url_for,session
from flask import request
import sqlite3


app = Flask(__name__)


@app.route('/admin-log-out',methods = ['POST'])
def Admin_Log_out():
    if request.method == 'POST':
        session.clear()
        
        return redirect('/')
    
    else:
        return 404 

@app.route('/admin')
def Admin_Page ():
    
    try:
        Name = session['Admin_Name']
        Last = session['Admin_Last']
        Email = session['Admin_Email']
        
        conn = sqlite3.connect('user.db')
        
        c = conn.cursor()
        
        c.execute("SELECT * FROM user_info")
        data = c.fetchall()
        
        data = len(data)

    
        return render_template ('admin.html',Name = Name,Last = Last,Email = Email,data = data)
    
    except:
        return redirect('/login')
        
@app.route('/delete',methods=['POST'])
def Delete_Account():
    name = session['Name']
    password = session['Password']
    
    conn = sqlite3.connect('user.db')
    
    c = conn.cursor()
    
    c.execute("DELETE FROM user_info WHERE Name = ? AND Password = ?",(name,password,))
    conn.commit()
    
    conn.close()
    
    session.clear()
    
    return redirect('/')
    
@app.route('/update',methods=['POST'])
def Update ():
    Name = request.form['Name']
    Last = request.form['Last']
    Email = request.form['Email']
    Lang = request.form['Lang']
    Topic = request.form['Topic']
    
    
    if Name and Last and Email and Topic and Lang:
        if Name.isdigit() != True and Last.isdigit() != True:
    
            if '@' in Email and '.com' in Email:
                user = True
            else:
                user = False
        else:
            user = False
            
        if user:
            db_name = session['Name']
            db_password = session['Password']
            
            conn = sqlite3.connect('user.db')
            
            c = conn.cursor()
            
            c.execute('UPDATE user_info SET Name = ? ,Last_name = ?,Email = ?,Language = ?,Radio = ? WHERE Name = ? AND Password = ?',
                      (Name,Last,Email,Lang,Topic,db_name,db_password,))
            
            conn.commit()
    
            conn.close()
            
            session.clear()
            
            session['Name'] = Name
            session['Last'] = Last
            session['Email'] = Email
            session['Lang'] = Lang
            session['Topic'] = Topic
            session['Password'] = db_password
            
            return redirect('/')
        
        else:
            return Error("the data is invalid please check before enter ")
 
@app.route('/logout')
def Log_out ():
    session.clear()
    return redirect('/')

@app.route("/")
def Main_Page():
    try:
        Name = session['Name']
        Email = session['Email']
        Last = session['Last']
        Lang = session['Lang']
        Topic = session['Topic']
        Account = True
    except:
        Account = False

    
    if Account:    
        return render_template("main.html",Account = Account,NaMe = str(Name),EmAiL = str(Email),LaSt = Last,LaNg = Lang,ToPiC = Topic)
    else:
        return render_template('main.html',Account = Account)

@app.route("/error")
def Error(reason):
    return render_template("error.html",error_name = reason)


@app.route('/login-data',methods = ['POST'])
def Login_Data_Process():
    Name_Email = request.form["name_email"]
    Password = request.form['password']
    found = False
    
    
    if Password and Name_Email:
        if len(Password) > 6 and Name_Email.isdigit() != True:
            PASS = False
            Conn = sqlite3.connect("user.db")
            c = Conn.cursor()
            
            if "@" in Name_Email and ".com" in Name_Email:
                c.execute("SELECT * FROM user_info WHERE Email = ? AND Password =  ?",(Name_Email,Password,))
                data = c.fetchall()
                if data:
                    
                    PASS = data[0][3]
                    NAME = data[0][0]
                    EMAIL = data[0][2]
                    LAST = data[0][1]
                    LANG = data[0][4]
                    TOPIC = data[0][6]
                
                
                if data:
                    if data[0][2] == Name_Email:
                        found = True
                        
                    else:
                        found = False
                
                else:
                    found = False
                
            else:
                c.execute("SELECT * FROM user_info WHERE Name = ? AND Password = ?",(Name_Email,Password,))
                data = c.fetchall()
                
                if data:
                   
                    PASS = data[0][3]
                    NAME = data[0][0]
                    EMAIL = data[0][2]
                    LAST = data[0][1]
                    LANG = data[0][4]
                    TOPIC = data[0][6]
                
                
                if data:
                    if data[0][0] == Name_Email:
                        
                        found = True
                     
                    else:
                        found = False
                           
                    
                else:
                    found = False
                    

            if data:
                
                if PASS == Password:
                    Pass_Found = True
                    
                else:
                    Pass_Found = False
                
            else:
                Pass_Found = False
            
            
            if found and Pass_Found:
                
                if data[0][7] == 'Normal':
                    session['Name'] = NAME
                    session['Last'] = LAST
                    session['Email'] = EMAIL
                    session['Lang'] = LANG
                    session['Topic'] = TOPIC
                    session['Password'] = PASS
                    
                    return redirect('/')
                
                else:
                    session['Admin_Name'] = NAME
                    session['Admin_Last'] = LAST
                    session['Admin_Email'] = EMAIL
                    session['Admin_Password'] = PASS
                    
                    return redirect('/admin')
            
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
            
            c.execute("CREATE TABLE IF NOT EXISTS user_info (Name , Last_name , Email , Password , Language , Status , Radio, Type)")
            
            conn.commit()
            
            c.execute(""" INSERT INTO user_info (Name , Last_name , Email , Password , Language , Status , Radio, Type) 
                        VALUES ( :Name , :Last_name , :Email , :Password , :Language , :Status , :Radio , 'Normal')
                        
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
    app.secret_key = 'secretkeynone'
    app.run(
        debug=True,
        host='127.0.0.1',
        port=5001
            
            )
 