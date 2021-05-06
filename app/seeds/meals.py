from app.models import db, Meal, user_meals


def seed_meals():
    return


def undo_meals():
    db.session.execute('TRUNCATE meals RESTART IDENTITY CASCADE;')
    db.session.commit()


def seed_user_meals():
    return


def undo_user_meals():
    db.session.execute('TRUNCATE user_meals RESTART IDENTITY CASCADE;')
    db.session.commit()
