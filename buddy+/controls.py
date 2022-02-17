from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

def track_current_user(method, username=''):
    if method == 'add':
        f = open('username.txt', 'a')
        f.write(username)
        f.close
        return
    elif method == 'del':
        f = open('username.txt', 'w')
        f.write("")
        f.close
        return
    elif method == 'curr':
        f = open('username.txt', 'r')
        for row in f:
            return row
    else:
        return

def add_interests(user, interest_list):
    from models import Interests
    for interest in interest_list:
        inter_to_add=Interests.query.filter_by(interest_name=interest).first()
        user.interested_in.append(inter_to_add)
    return

def update_user_info(form):
    from models import User
    user = User.query.filter_by(username=track_current_user('curr')).first()
    if form.chosen_interests.data != None:
        add_interests(user, form.chosen_interests.data)
    if form.is_buddy.data != user.is_buddy:
        user.is_buddy = form.is_buddy.data
    if form.is_student.data != form.is_student.data:
        user.is_student = form.is_student.data
    if form.current_uni.data != None:
        user.current_uni = form.current_uni.data
    if form.email.data != None:
        user.email = form.email.data
    return user
    
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

def get_interests():
    from models import Interests
    interests = Interests.query.all()
    inter_list = []
    for intr in interests:
        inter_list.append(intr.interest_name)
    return inter_list

def get_user_info(usrnm):
    from models import User
    user = User.query.filter_by(username=usrnm).first()
    return user    

def check_user_authenticity(uname, psswrd):
    from models import User
    user = User.query.filter_by(username=uname).first()
    if not user or not check_password_hash(user.password, psswrd):
        return False
    else:
        track_current_user('add', uname)
        return True

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

def database_control(inter_id):
    conn = None
    try:
        conn = sqlite3.connect('app.db')
    except:
        error=error
        print(error)
    cur = conn.cursor()
    cur.execute("SELECT user_id, interest_id FROM interest_table WHERE interest_id =:intr_id ", {"intr_id": str(inter_id)})
    return cur.fetchall()

def process_search(form):
    from models import User, Interests
    city = form.chosen_city.data
    interest = form.chosen_interest.data
    selected_intrst = Interests.query.filter_by(interest_name=interest).first()
    final_users = database_control(selected_intrst.interest_id)
    buddy_list = []
    for x in final_users:
        user = User.query.filter_by(user_id=x[0]).first()
        if user.current_location == city:
            if track_current_user('curr') == (user.username):
                pass
            else:
                buddy_list.append(user)
        else:
            pass
    return buddy_list