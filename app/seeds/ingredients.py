from app.models import db, Ingredient, MealIngredient

def seed_ingredients():
    ingredient1 = Ingredient(
        name='apples', type='fruit')
    ingredient2 = Ingredient(
        name='oranges', type='fruit')
    ingredient3 = Ingredient(
        name='bananas', type='fruit')
    ingredient4 = Ingredient(
        name='blueberries', type='fruit')
    ingredient5 = Ingredient(
        name='raspberries', type='fruit')
    ingredient6 = Ingredient(
        name='coconuts', type='fruit')
    ingredient7 = Ingredient(
        name='cantaloupes', type='fruit')
    ingredient8 = Ingredient(
        name='cherries', type='fruit')
    ingredient9 = Ingredient(
        name='blackberries', type='fruit')
    ingredient10 = Ingredient(
        name='steak', type='protein')
    ingredient11 = Ingredient(
        name='chicken', type='protein')
    ingredient12 = Ingredient(
        name='salmon', type='protein')
    ingredient13 = Ingredient(
        name='ground beef', type='protein')
    
    db.session.add(ingredient1)
    db.session.add(ingredient2)
    db.session.add(ingredient3)
    db.session.add(ingredient4)
    db.session.add(ingredient5)
    db.session.add(ingredient6)
    db.session.add(ingredient7)
    db.session.add(ingredient8)
    db.session.add(ingredient9)
    db.session.add(ingredient10)
    db.session.add(ingredient11)
    db.session.add(ingredient12)
    db.session.add(ingredient13)
    

    db.session.commit()

def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
    

def seed_meal_ingredients():
    return
    # one = MealIngredient(meal_id=1, ingredient_id=1, ingredient_quantity=0.5)

    # db.session.add(one)

    # db.session.commit()


def undo_meal_ingredients():
    return
