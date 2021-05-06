from app.models import db, Ingredient

def seed_ingredients():
    return
    # demo = User(username='Clif', email='Clif@Clif.com',
    #            password='Clif')

    # db.session.add(demo)

    # db.session.commit()

def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
    

def seed_meal_ingredients():
    return


def undo_meal_ingredients():
    return