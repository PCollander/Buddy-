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
viina = Interests(interest_descr="Drinking alcohol beverages", interest_name="Alcohol")
gym = Interests(interest_descr="Going to the gym", interest_name="Gym")
party = Interests(interest_descr="Attending different parties", interest_name="Partying")

viina.chosen_by_users.append(pyry)
football.chosen_by_users.append(pyry)
gym.chosen_by_users.append(pyry)
party.chosen_by_users.append(pyry)
coding.chosen_by_users.append(anda)
coding.chosen_by_users.append(rares)
party.chosen_by_users.append(rares)
party.chosen_by_users.append(anda)
rares.interested_in.append(viina)

db.session.add(pyry)
db.session.add(rares)
db.session.add(anda)
db.session.add(viina)
db.session.add(football)
db.session.add(coding)
db.session.add(party)
db.session.add(gym)


db.session.commit()