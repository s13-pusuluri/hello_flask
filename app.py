from flask import Flask
from flask import Flask , render_template , request
from flask import Flask , redirect, url_for
import sqlite3

app = Flask(__name__)

# Home Page route
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/landing")
def landing():
    return render_template("landing.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/")
def home():
    return "Hello, Flask.!"

# Route to form used to add a new user for the website


def create_conn():
    conn = sqlite3.connect('database.db')  
    return conn
    
conn = create_conn()
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username txt, password text)''')
conn.commit()
conn.close()


# Route to add a new record (INSERT) user data to the database - Login USER
@app.route("/login", methods = ['POST', 'GET'])
def login1():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            # Connect to SQLite3 database and execute the INSERT
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (username, password) VALUES (?,?)",(username, password))
                con.commit()
                msg = "Record successfully added to database"
        except:
            con.rollback()
            msg = "Error in the INSERT"

        finally:
            con.close()
            # # Send the transaction message to result.html
        return render_template('index.html',msg=msg)
    
    
    
    
# connecting to signup page
def create_conn():
    conn = sqlite3.connect('newusers.db')  
    return conn
    
conn = create_conn()
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users1
             (username txt, email, password text, confirmPassword text )''')
conn.commit()
conn.close()




@app.route("/signup", methods = ['POST', 'GET'])
def signup1():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            confirmPassword = request.form['ConfirmPassword']

            # Connect to SQLite3 database and execute the INSERT
            with sqlite3.connect('newusers.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users1 (username, email, password, confirmPassword) VALUES (?,?,?,?)",(username, email, password, confirmPassword))
                con.commit()
                msg = "Record successfully added to database"
        except:
            con.rollback()
            msg = "Error in the INSERT"

        finally:
            con.close()
            # # Send the transaction message to result.html
        return render_template('index.html',msg=msg)
