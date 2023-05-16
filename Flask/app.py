
from flask import Flask, redirect, render_template,jsonify,session
from flask import request
import sqlite3
import csv

app = Flask(__name__)


@app.route('/return-csv-data',methods = ['POST'])
def Return_Csv_Data ():
    index = request.get_json()
    
    if int(index['return']):
        conn = sqlite3.connect('user.db')
        c = conn.cursor()

        try:
            c.execute("SELECT * FROM user_csv")
        
            user_data = c.fetchall()
            
            if not user_data:
            
                return jsonify({"exist" : False})
            
        except:
            
            return jsonify({"exist" : False})
        
        c.close()
    
    num = int(index['return'])-1
    
    
    data = {
        'exist' : True,
        'Name' : user_data[num][0],
        'Last' : user_data[num][1],
        'Email' : user_data[num][2],
        'Lang' : user_data[num][3],
        'Status' : user_data[num][4],
        'Topic' : user_data[num][5],
    }
    
    return jsonify(data)
    

@app.route('/import-csv',methods = ['POST'])
def Import_Csv():

    filename = request.files["csv_file"]
    file_text = filename.read().decode('utf-8')
    
    Reader = csv.DictReader(file_text.splitlines())
    
    data = []

    for each_user in Reader:
        data.append(each_user)
        

            
    conn = sqlite3.connect("user.db")
    c = conn.cursor()  
            
    for user in data:
        Name = user['Name'].lower()
        Last = user['Last']
        Email = user['Email']
        Lang = user['Lang']
        Status = user['Status']
        Topic = user['Topic']
        
        c.execute("CREATE TABLE IF NOT EXISTS user_csv (Name , Last,Email,Lang,Status,Topic)")
        
        c.execute("SELECT * FROM user_csv WHERE Name = ? AND Email = ?",(Name,Email,))
        fetch_data = c.fetchall()
        
        if fetch_data :
            pass
        
        else:
            
            c.execute("INSERT INTO user_csv(Name ,Last,Email,Lang,Status,Topic) VALUES (?,?,?,?,?,?)",
                      (Name,Last,Email,Lang,Status,Topic))
            
            conn.commit()
            
    conn.close()
    
    print(data)
    return redirect('/admin')
        

@app.route('/return-data',methods = ['POST','GET'])
def Return_Data ():
    index = request.get_json()
    
    if int(index['return']):
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
    
        c.execute("SELECT * FROM user_info WHERE Type = 'Normal'")
        
        user_data = c.fetchall()
        
        c.close()
    
    num = int(index['return'])-1
    
    data = {
        'Name' : user_data[num][0],
        'Last' : user_data[num][1],
        'Email' : user_data[num][2],
        'Lang' : user_data[num][4],
        'Type' : user_data[num][5],
        'Topic' : user_data[num][6],
    }
    
    return jsonify(data)
    
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
        
        
        try:
            c.execute("SELECT * FROM user_csv")
            csv_data = c.fetchall()
            csv_data = len(csv_data)
        except:
            csv_data = 0
        
        c.execute("SELECT * FROM user_info")
        data = c.fetchall()
        
        data = len(data)-1

        c.close()
        return render_template ('admin.html',Name = Name,Last = Last,Email = Email,data = data,csv_data = csv_data)
    
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
    return redirect('/sign-up')

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
                Name_Email = Name_Email.lower()
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
    
    Name = request.form['Name'].lower()
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
 