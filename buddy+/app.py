"""
Politecnico di Torino, Information Systems, Semester of 2021-2022
Group 14, Buddy+

The application allows users to register for our service that connects people
from different cities to ensure rewarding experiences in the chosen city. The
users filter Buddies based on their preferred city and activity and then choose
the most suiting Buddy from the resulting list provided by the service. The 
service is free for users with a student status and chargeable for non-students
users.

The application follows MVC-architecture with the files app.py (views), 
models.py (models) & controls.py (controls).

"""

from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from config import secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from controls import process_search, read_new_user_info, add_interests, \
    check_user_authenticity, track_current_user, update_user_info, \
        get_user_info


# checks if the user is logged in or not, redirects accordingly
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


# Function that handles user registration or redirets them  to the login page  
# if they are already authenticated 
@app.route('/register', methods=['GET','POST'])
def register():
    error=None
    from forms import RegisterForm
    reg_form = RegisterForm()
    # Specific checking if the user is logged in or not. Redirects if is logged
    # in
    if 'logged_in' in session.values():
        if session['logged_in'] == True:
            return redirect(url_for('homepage'))
        else:
            return render_template('registration.html', form=reg_form)
    else:
        if request.method == 'POST' and reg_form.validate():
            # Passes form information to handler function. Returns User-object
            user = read_new_user_info(reg_form)
            # Reads and adds the chosen interests to the User
            interest_list = reg_form.chosen_interests.data
            add_interests(user, interest_list)
            # Save data to database and allow user to login after sign up
            current_db_sessions = db.session.object_session(user)
            current_db_sessions.add(user)
            current_db_sessions.commit()
            return render_template('login2.html')
        error=reg_form.errors.items()
        return render_template('registration.html', error=error, form=reg_form)


# Presents the user with a search form to query Buddies with desired qualities
@app.route('/search_view', methods=['GET', 'POST'])
@login_required
def search_view():
    error=None
    from forms import SearchForm
    search_form = SearchForm()
    if request.method == 'POST' and search_form.validate():
        # Passes the form inputs to a function that does processes the search,
        # returns a list of Objects if the list is not empty
        users = process_search(search_form)
        return render_template('search_results.html', users=users)
    error=search_form.errors.items()
    return render_template('search_view.html', form=search_form, error=error)


# Shows a chosen user more specificly from the query result list
@app.route('/show_user', methods=['GET', 'POST'])
@login_required
def show_user():
    # Passes the username of the chosen user to a function that fetches the 
    # users information
    user_info = get_user_info(request.form.get('username'))
    return render_template('show_user.html', user_info=user_info)


# Allows the user to modify their information
@app.route('/modify_information', methods=['GET', 'POST'])
@login_required
def modify_information():
    error=None
    from forms import ModifyInfo
    mod_info = ModifyInfo()
    if request.method == 'POST' and mod_info.validate():
        # Passes the form inputs to the function that does the updating
        user = update_user_info(mod_info)
        # Saves the database modifications
        current_db_sessions = db.session.object_session(user)
        current_db_sessions.commit()
        return redirect(url_for('homepage'))
    error=mod_info.errors.items()
    return render_template('modify_information.html', mod_info=mod_info,\
         error=error)


# Logs the user in and redirects to the home page if status is already logged 
# in
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # Specific checking if the user is logged in or not. Redirects if is logged
    # in
    if 'logged_in' in session.values():
        if session['logged_in'] == True:
            return redirect(url_for('homepage'))
    if request.method == 'POST':
        # Passes the form inputs to a function that checks the credencial 
        # validity. Redirects accordingly or informs of an error
        if not check_user_authenticity(request.form.get('username'), 
                request.form.get('password')):
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('homepage'))
    return render_template('login2.html', error=error)


# Function for logging out the user
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    track_current_user('del')
    return render_template('login2.html')


# View homepage when logged in
@app.route('/homepage')
@login_required
def homepage():
    return render_template("landingpage.html")


# View the initial page when user isn't logged in. Redirect if user is logged 
# in
@app.route('/')
def index():
    print(session['logged_in'])
    if 'logged_in' in session.values():
        if session['logged_in'] == True:
            return redirect(url_for('homepage'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



