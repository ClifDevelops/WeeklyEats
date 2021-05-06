# from werkzeug.security import generate_password_hash
from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    user = User(username='Clif', email='Clif@Clif.com',
                password='Clif')
    user2 = User(username='Bri', email='Bri@Bri.com',
                password='Bri')
    user3 = User(username='Robbie', email='Robbie@Robbie.com',
                password='Robbie')

    db.session.add(user)
    db.session.add(user2)
    db.session.add(user3)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
