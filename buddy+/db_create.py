"""
Politecnico di Torino, Information Systems, Semester of 2021-2022
Group 14, Buddy+

Used to initialize the database.

"""


from app import db
from models import User, Interests
import datetime
from werkzeug.security import generate_password_hash


db.drop_all()
db.create_all()

anda = User(username="Anda420", email="mitä@missä.com", password=generate_password_hash("pront0", method='sha256'), name="Anda", surname="Arghir", current_location="Turin", nationality="Romanian", date_of_birth=(datetime.datetime(int("1999"), int("1"), int("1"))), is_buddy=False, is_student=True, current_uni="Romanian army school", mother_tongue="Romanian")
pyry = User(username="Spyrde1349", email="joku@jossain.com", password=generate_password_hash("morjesta", method='sha256'), name="Pyry", surname="Collander", current_location="Turin", nationality="Finnish", date_of_birth=(datetime.datetime(int("1900"), int("1"), int("1"))), is_buddy=True, is_student=True, current_uni="TUNI", mother_tongue="Finnish")
rares = User(username="Rares_Beast", email="ehkä@joskus.com", password=generate_password_hash("jeesjees", method='sha256'), name="Rares", surname="Birzenau", current_location="Turin", nationality="Romanian", date_of_birth=(datetime.datetime(int("1800"), int("1"), int("1"))), is_buddy=True, is_student=True, current_uni="Royal Romanian Uni", mother_tongue="Romanian")
coding = Interests(interest_descr="Likes to code", interest_name="Coding")
football = Interests(interest_descr="Playing football", interest_name="Football")
gym = Interests(interest_descr="Going to the gym", interest_name="Gym")
party = Interests(interest_descr="Attending different parties", interest_name="Partying")
cooking = (Interests(interest_descr="Likes cooking different meals", interest_name="Cooking"))
drawing = (Interests(interest_descr="Likes to draw", interest_name="Drawing"))
culture = (Interests(interest_descr="Likes to enjoy culture", interest_name="Culture"))
icehockey = (Interests(interest_descr="Likes to play ice hockey", interest_name="Ice hockey"))
photography = (Interests(interest_descr="Enjoys photography", interest_name="Photography"))
music = (Interests(interest_descr="Likes to enjoy music", interest_name="Music"))
sightseeing = (Interests(interest_descr="Likes to go sightseeing", interest_name="Sightseeing"))
videogames = (Interests(interest_descr="Likes to play video games", interest_name="Video gaming"))
sport = (Interests(interest_descr="Likes sports in general", interest_name="Sports"))
debate = (Interests(interest_descr="Likes deabting on different topics", interest_name="Debating"))
forgn_lnggs = (Interests(interest_descr="Likes foreign languages", interest_name="Foreign languages"))


football.chosen_by_users.append(pyry)
gym.chosen_by_users.append(pyry)
party.chosen_by_users.append(pyry)
coding.chosen_by_users.append(anda)
coding.chosen_by_users.append(rares)
party.chosen_by_users.append(rares)
party.chosen_by_users.append(anda)
cooking.chosen_by_users.append(anda)
cooking.chosen_by_users.append(pyry)
drawing.chosen_by_users.append(rares)
drawing.chosen_by_users.append(pyry)
culture.chosen_by_users.append(anda)
culture.chosen_by_users.append(rares)
icehockey.chosen_by_users.append(pyry)
photography.chosen_by_users.append(anda)
photography.chosen_by_users.append(pyry)
music.chosen_by_users.append(rares)
music.chosen_by_users.append(pyry)
music.chosen_by_users.append(anda)
sightseeing.chosen_by_users.append(anda)
sightseeing.chosen_by_users.append(rares)
sightseeing.chosen_by_users.append(pyry)
videogames.chosen_by_users.append(pyry)
videogames.chosen_by_users.append(rares)
videogames.chosen_by_users.append(anda)
sport.chosen_by_users.append(pyry)
sport.chosen_by_users.append(anda)
debate.chosen_by_users.append(anda)
debate.chosen_by_users.append(rares)
forgn_lnggs.chosen_by_users.append(rares)
forgn_lnggs.chosen_by_users.append(anda)

db.session.add(pyry)
db.session.add(rares)
db.session.add(anda)
db.session.add(football)
db.session.add(coding)
db.session.add(party)
db.session.add(gym)
db.session.add(cooking)
db.session.add(drawing)
db.session.add(culture)
db.session.add(icehockey)
db.session.add(photography)
db.session.add(music)
db.session.add(sightseeing)
db.session.add(videogames)
db.session.add(sport)
db.session.add(debate)
db.session.add(forgn_lnggs)



db.session.commit()