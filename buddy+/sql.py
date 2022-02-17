import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""DROP TABLE users""")
    c.execute("""DROP TABLE interests""")
    c.execute("""CREATE TABLE users(username TEXT, email TEXT, 
        password TEXT, name TEXT, surname TEXT, current_location TEXT, 
        nationality TEXT, date_of_birth TEXT, is_buddy INTEGER, 
        is_student INTEGER, current_uni TEXT, mother_tongue TEXT)""")
    c.execute("""CREATE TABLE interests(interest_descr TEXT, 
        interest_name TEXT)""")
    c.execute('INSERT INTO users VALUES("Spyrde1349", "joku@jossain.com", "morjesta", "Pyry", "Collander", "Turin", "Finnish", "1.1.1900", "1", "1", "TUNI", "Finnish")')
    c.execute('INSERT INTO users VALUES("Rares_Beast", "ehkä@joskus.com", "jeesjees", "Rares", "Birzenau", "Turin", "Romanian", "1.1.1800", "1", "1", "Royal Romanian Uni", "Romanian")')
    c.execute('INSERT INTO interests VALUES("Playing football", "Football")')
    c.execute('INSERT INTO interests VALUES("Drinking alcohol beverages", "Alcohol")')
    c.execute('INSERT INTO interests VALUES("Going to the gym", "Gym")')
    c.execute('INSERT INTO interests VALUES("Attending different parties", "Partying")')