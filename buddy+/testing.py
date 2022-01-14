from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
#login to-be
#redirect to home page if status is logged in
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)


@app.route('/home')
#redirect here if user tries to go to '/'
#require status to be logged in
def homepage():
    return render_template("welcome.html")

if __name__ == '__main__':
    app.run(debug=True)



