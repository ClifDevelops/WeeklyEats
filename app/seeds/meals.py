from app.models import db, Meal, UserMeal


def seed_meals():
    meal1 = Meal(name='Spaghetti', cuisine='Italian',
                recipe='''1. Combine ground beef, onion, garlic, and green pepper in a large saucepan. Cook and stir until meat is brown and vegetables are tender. Drain grease.
    2. Stir diced tomatoes, tomato sauce, and tomato paste into the pan. Season with oregano, basil, salt, and pepper. Simmer spaghetti sauce for 1 hour, stirring occasionally.
    3. Boil pasta until desired finish. Drain and combine with sauce.
    ''')
    meal2 = Meal(name='Steak and Potatoes', cuisine='American',
                recipe= '''1. Season the steak with salt, pepper, and any other desired spice.
                2. Prepare the potatoes, either boiled and mashed or cut into a large dice and roasted with herbs and spices.
                3. Cook the steak. Get a nice sear and bring up to a medium temperature.
                4. Roast either asparagus or broccoli as a vegetable for the side.
                ''')

    db.session.add(meal1)
    db.session.add(meal2)

    db.session.commit();

def undo_meals():
    db.session.execute('TRUNCATE meals RESTART IDENTITY CASCADE;')
    db.session.commit()


def seed_user_meals():
    user_meal1 = UserMeal(user_id=1, meal_id=1)
    user_meal2 = UserMeal(user_id=1, meal_id=2)

    db.session.add(user_meal1)
    db.session.add(user_meal2)

    db.session.commit()


def undo_user_meals():
    db.session.execute('TRUNCATE user_meals RESTART IDENTITY CASCADE;')
    db.session.commit()
