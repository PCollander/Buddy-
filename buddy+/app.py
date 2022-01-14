from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

app = Flask(__name__)
app.secret_key = "ThisIsTHeKeyThatWillBeMovedToASecureLocationInTheFuture"
app.database = "sample.db"

#@app.route('/signup', methods=['GET','POST'])
#def signup():

#checks if the user is logged in or not, redirects accordingly
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#logs user in
#redirect to home page if status is logged in
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)

#function for logging out the user
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You were just logged out")
    return redirect(url_for('login'))

#redirect here if user tries to go to '/'
#require status to be logged in
@app.route('/homepage')
@login_required
def homepage():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template("landingpage.html", posts=posts)

def connect_db():
    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True)



