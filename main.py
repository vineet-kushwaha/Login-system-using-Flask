from flask import Flask,render_template,request,redirect,session
import mysql.connector
import os

app= Flask(__name__)
app.secret_key=os.urandom(24)

conn = mysql.connector.connect(host='localhost',user='DB_UserName',password='DB_password',database='users')
cursor = conn.cursor()


@app.route('/')
def login():
    if 'user_id' in session:
        return redirect('/home')
    else:
        return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')


@app.route('/login_validation', methods=['POST'] )
def login_validation():
    id = request.form.get('mail','')
    password=request.form.get('pass')
    
    cursor.execute("""SELECT * FROM `login` WHERE `email` LIKE '{}' AND `password` LIKE'{}'""".format(id,password))
    users = cursor.fetchall()
    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/home')
    else:
        return redirect('/')


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        uname=request.form.get('uname')
        uid=request.form.get('umail')
        upass=request.form.get('upass')
        cursor.execute("""INSERT INTO `login` (`id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')""".format(uname,uid,upass))
        conn.commit()

        cursor.execute("""SELECT * FROM `login` WHERE `email` LIKE '{}'""".format(uid))
        my_user = cursor.fetchall()
        print (my_user)
        session['user_id']=my_user[0][0]
        return redirect('/home')
    except:
        return 'use a different email click here ---> <a href="/register">register</a>'
    

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)