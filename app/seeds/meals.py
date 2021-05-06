from app.models import db, Meal, UserMeal


def seed_meals():
    meal1 = Meal(name='Spaghetti', cuisine='Italian',
    recipe=''' 1. Boil Noodles
    2. Heat up sauce.
    3. Combine.
    ''')

    db.session.add(meal1)

    db.session.commit();

def undo_meals():
    db.session.execute('TRUNCATE meals RESTART IDENTITY CASCADE;')
    db.session.commit()


def seed_user_meals():
    one = UserMeal(user_id=1, meal_id=1)

    db.session.add(one)

    db.session.commit()


def undo_user_meals():
    db.session.execute('TRUNCATE user_meals RESTART IDENTITY CASCADE;')
    db.session.commit()
