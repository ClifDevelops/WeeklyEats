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
    ingredient14 = Ingredient(
        name='pork belly', type='protein')
    ingredient15 = Ingredient(
        name='pork loin', type='protein')
    ingredient16 = Ingredient(
        name='sausage', type='protein')
    ingredient17 = Ingredient(
        name='sausage (ground)', type='protein')
    ingredient18 = Ingredient(
        name='pepperoni', type='protein')
    ingredient19 = Ingredient(
        name='ham', type='protein')
    ingredient20 = Ingredient(
        name='ham (deli)', type='protein')
    ingredient21 = Ingredient(
        name='bacon', type='protein')
    ingredient22 = Ingredient(
        name='turkey', type='protein')
    ingredient23 = Ingredient(
        name='turkey (deli)', type='protein')
    ingredient24 = Ingredient(
        name='chicken tenders', type='protein')
    ingredient25 = Ingredient(
        name='chicken breasts', type='protein')
    ingredient26 = Ingredient(
        name='chicken thighs', type='protein')
    ingredient27 = Ingredient(
        name='chicken wings', type='protein')
    
    
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
    db.session.add(ingredient14)
    db.session.add(ingredient15)
    db.session.add(ingredient16)
    db.session.add(ingredient17)
    db.session.add(ingredient18)
    db.session.add(ingredient19)
    db.session.add(ingredient20)
    db.session.add(ingredient21)
    db.session.add(ingredient22)
    db.session.add(ingredient23)
    db.session.add(ingredient24)
    db.session.add(ingredient25)
    db.session.add(ingredient26)
    db.session.add(ingredient27)
    

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
