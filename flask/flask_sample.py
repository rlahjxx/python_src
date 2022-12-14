
from flask import Flask, session, render_template, redirect, request, url_for
from flask_mysqldb import MySQL



mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pydata'
app.secret_key = 'ABCDEF'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    error = None

    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']

        conn = mysql.connection
        cursor = conn.cursor()

        sql = "SELECT id, name FROM users WHERE id = '%s' AND passwd = '%s' " % (id, pw)

        # print(sql)
        # cursor.execute("set names utf8")
        cursor.execute(sql)

        data = cursor.fetchall()
        print("data == ",data)
        cursor.close()
        conn.close()

        for row in data:
            r_id = row[0]
            r_name = row[1]

        if r_id:
            session['login_id'] = r_id
            return redirect(url_for('home',name=name))
        else:
            error = 'invalid input data detected !'

    return render_template('main.html', error=error)


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form['regi_id']
        pw = request.form['regi_pw']
        name = request.form['regi_name']

        conn = mysql.connection
        cursor = conn.cursor()

        sql = "INSERT INTO users (id,password,name) VALUES ('%s', '%s', '%s')" % (id, pw, name)
        cursor.execute(sql)

        data = cursor.fetchall()

        if not data:
            conn.commit()
            return redirect(url_for('main'))
        else:
            conn.rollback()
            return "Register Failed"

        cursor.close()
        conn.close()

    return render_template('register.html', error=error)

@app.route('/home.html/<name>', methods=['GET', 'POST'])
def home(name):
    error = None
    return render_template('home.html', name=name)
 

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)


# In[ ]:





# In[ ]:




