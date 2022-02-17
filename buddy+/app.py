from flask import Flask, render_template, redirect, url_for, request, session,\
    flash
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
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# function that handles user registration or redirets them if they are 
# authenticated already
@app.route('/register', methods=['GET','POST'])
def register():
    error=None
    from forms import RegisterForm
    reg_form = RegisterForm()
    if 'logged_in' in session.values():
        if session['logged_in'] == True:
            return redirect(url_for('homepage'))
        else:
            return render_template('registration.html', form=reg_form)
    else:
        if request.method == 'POST' and reg_form.validate():
            user = read_new_user_info(reg_form)
            interest_list = reg_form.chosen_interests.data
            add_interests(user, interest_list)   
            current_db_sessions = db.session.object_session(user)
            current_db_sessions.add(user)
            current_db_sessions.commit()
            flash(f"User {reg_form.username.data} succesfully created!")
            return render_template('login2.html')
        error=reg_form.errors.items()
        return render_template('registration.html', error=error, form=reg_form)

@app.route('/search_view', methods=['GET', 'POST'])
@login_required
def search_view():
    error=None
    from forms import SearchForm
    search_form = SearchForm()
    if request.method == 'POST' and search_form.validate():
        users = process_search(search_form)
        return render_template('search_results.html', users=users)
    error=search_form.errors.items()
    return render_template('search_view.html', form=search_form, error=error)

app.route('search_results', methods=['GET', 'POST'])
@login_required
def search_results():
    if request.method == 'POST':
        user_info = get_user_info(request.form.get('username'))
        return render_template('show_user.html', user_info=user_info)
    return render_template('search_results.html')

@app.route('/show_user', methods=['GET', 'POST'])
@login_required
def show_user():
    error=None
    if request.method == 'GET':
        user_info = get_user_info(request.form.get('username'))
        return render_template('show_user.html', user_info=user_info)
    return render_template('show_user.html', error=error)

@app.route('/modify_information', methods=['GET', 'POST'])
@login_required
def modify_information():
    error=None
    from forms import ModifyInfo
    mod_info = ModifyInfo()
    if request.method == 'POST' and mod_info.validate():
        user = update_user_info()
        current_db_sessions = db.session.object_session(user)
        current_db_sessions.commit()
        flash('Your information was updated succesfully!')
        render_template('modify_information.html')
    error=mod_info.errors.items()
    render_template('modify_information.html', error=error)



# logs user in
# redirect to home page if status is logged in
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not check_user_authenticity(request.form.get('username'), 
                request.form.get('password')):
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('homepage'))
    return render_template('login2.html', error=error)


# function for logging out the user
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    track_current_user('del')
    flash("You were just logged out")
    return render_template('login2.html')


# redirect here if user tries to go to '/'
# require status to be logged in
@app.route('/homepage')
@login_required
def homepage():
    return render_template("landingpage.html")


if __name__ == '__main__':
    app.run(debug=True)



