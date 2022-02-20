"""
Politecnico di Torino, Information Systems, Semester of 2021-2022
Group 14, Buddy+

The controls file of the service.
"""


from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


# Poor mans tracking function for checking the username of the user
# currently logged in. In production would have to be replaced
def track_current_user(method, username=''):
    # Writes the users name in a file upon loggin in
    if method == 'add':
        f = open('username.txt', 'a')
        f.write(username)
        f.close
        return
    # Deletes the users name from the file upon loggin out
    elif method == 'del':
        f = open('username.txt', 'w')
        f.write("")
        f.close
        return
    # Returns the name of the currently logged in user
    elif method == 'curr':
        f = open('username.txt', 'r')
        for row in f:
            return row
    else:
        return


# Takes the registering user and their chosen interests as attributes and adds
# the interests to the user
def add_interests(user, interest_list):
    from models import Interests
    for interest in interest_list:
        inter_to_add=Interests.query.filter_by(interest_name=interest).first()
        user.interested_in.append(inter_to_add)
    return


# Gets the updated information of a user and returns the user with new 
# information connected to the User Object
def update_user_info(form):
    from models import User
    # Get current users information using the tracking function
    user = User.query.filter_by(username=track_current_user('curr')).first()
    """
    This section is under construction for future implementation
    
    user_id = user.user_id
    if form.chosen_interests.data != None:
        remove_interest(user_id)
        add_interests(user, form.chosen_interests.data)
    """
    user.is_buddy = form.is_buddy.data
    user.is_student = form.is_student.data
    user.current_uni = form.current_uni.data
    return user


"""
Under construction for future implementaion:
Removes the previously chosen interests from the user upon information 
modification.

def remove_interest(user):
    conn = None
    try:
        conn = sqlite3.connect('app.db')
    except:
        error=error
    cur = conn.cursor()
    cur.execute("DELETE FROM interest_table WHERE user_id =:user", {"user": str(user)})
    return
"""


# Receives registration information and associates with a User object. Returns
# the freshly created User object
def read_new_user_info(reg_form):
    from models import User
    user = User(username=reg_form.username.data, 
            password=generate_password_hash(reg_form.password.data, method='sha256'),
            email=reg_form.email.data, name=reg_form.name.data, 
            surname=reg_form.surname.data, 
            current_location=reg_form.current_location.data,
            nationality=reg_form.nationality.data, 
            date_of_birth=reg_form.date_of_birth.data,
            is_buddy=reg_form.is_buddy.data, 
            is_student=reg_form.is_student.data, 
            current_uni=reg_form.current_uni.data, 
            mother_tongue=reg_form.mother_tongue.data)
    return user


# Returns all the interests from the database as a list object
def get_interests():
    from models import Interests
    interests = Interests.query.all()
    inter_list = []
    for intr in interests:
        inter_list.append(intr.interest_name)
    return inter_list


# Receives a username and return the corresponding User object
def get_user_info(usrnm):
    from models import User
    user = User.query.filter_by(username=usrnm).first()
    return user    


# Receives the username & password upon loggin in. Returns True if they check 
# out with the database. Otherwise returns False.
def check_user_authenticity(uname, psswrd):
    from models import User
    user = User.query.filter_by(username=uname).first()
    if not user or not check_password_hash(user.password, psswrd):
        return False
    else:
        # Adds name of the logging in user to the tracking file
        track_current_user('add', uname)
        return True


# Gets all the cities of registered users. Returns them as a list object
def get_cities():
    from models import User
    users = User.query.all()
    city_list = []
    for user in users:
        if user.current_location in city_list:
            pass
        else:
            city_list.append(user.current_location)
    return city_list


# Receives an interest id and returns all users who have the afore mentioned 
# interested chosen. Raw SQLite used to access the association table easier
def database_control(inter_id):
    conn = None
    try:
        conn = sqlite3.connect('app.db')
    except:
        error=error
    cur = conn.cursor()
    cur.execute("SELECT user_id, interest_id FROM interest_table WHERE interest_id =:intr_id ", {"intr_id": str(inter_id)})
    return cur.fetchall()


# Receives information from the search form an handles it. Returns a list 
# object populated with User objects
def process_search(form):
    from models import User, Interests
    # Get searched city & interest from the form
    city = form.chosen_city.data
    interest = form.chosen_interest.data
    selected_intrst = Interests.query.filter_by(interest_name=interest).first()
    # Get the users from the associaton table with the chosen interest
    final_users = database_control(selected_intrst.interest_id)
    buddy_list = []
    # Check that if the users with the interest are enrolled as buddies or not.
    # Also checks that the user isn't presented with themselves as a buddy 
    # option
    for x in final_users:
        user = User.query.filter_by(user_id=x[0]).first()
        if user.current_location == city and user.is_buddy == True:
            if track_current_user('curr') == (user.username):
                pass
            else:
                buddy_list.append(user)
        else:
            pass
    return buddy_list