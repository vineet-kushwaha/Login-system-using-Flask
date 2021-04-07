from flask import Flask,render_template,request
import mysql.connector

app= Flask(__name__)

#conn = mysql.connector.connect(host='',user='',password='',database='')
#cursor = conn.cursor()


@app.route('/')
def login():
    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login_validation', methods=['POST'] )
def login_validation():
    id = request.form.get('mail','')
    password=request.form.get('pass')
    
    return "Login sucessfull email: {} and password: {}".format(id,password)

    #cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE'{}'""".format(id,password))
    #users = cursor.fetchall()
    #if len(users)>0:
    #    return 'Login Sucessful'
    #else:
    #    return render_template('login.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    uname=request.form.get('uname')
    uid=request.form.get('uid')
    upass=request.form.get('upass')
    #cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`passwod`) VALUES (NULL,'{}','{}','{}')""".format(uname,uid,upass))
    #conn.commit()
    return 'User registered sucessfully. name: {}, email: {} and password: {}'.format(uname,uid,upass)






if __name__=="__main__":
    app.run(debug=True)