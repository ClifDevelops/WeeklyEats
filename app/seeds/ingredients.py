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
        name='kiwis', type='fruit')
    ingredient11 = Ingredient(
        name='plums', type='fruit')
    ingredient12 = Ingredient(
        name='grapes', type='fruit')
    ingredient13 = Ingredient(
        name='lemons', type='fruit')
    ingredient14 = Ingredient(
        name='limes', type='fruit')
    ingredient15 = Ingredient(
        name='grapefruits', type='fruit')
    ingredient16 = Ingredient(
        name='mangoes', type='fruit')
    ingredient17 = Ingredient(
        name='peaches', type='fruit')
    ingredient18 = Ingredient(
        name='tangerines', type='fruit')
    ingredient19 = Ingredient(
        name='pears', type='fruit')
    ingredient20 = Ingredient(
        name='pineapple', type='fruit')
    ingredient21 = Ingredient(
        name='pomegranate', type='fruit')
    ingredient22 = Ingredient(
        name='strawberries', type='fruit')
    ingredient23 = Ingredient(
        name='watermelon', type='fruit')


    ingredient24 = Ingredient(
        name='eggs', type='dairy')
    ingredient25 = Ingredient(
        name='whole milk', type='dairy')
    ingredient26 = Ingredient(
        name='oat milk', type='dairy')
    ingredient27 = Ingredient(
        name='almond milk', type='dairy')
    ingredient28 = Ingredient(
        name='yogurt', type='dairy')
    ingredient29 = Ingredient(
        name='sour cream', type='dairy')
    ingredient30 = Ingredient(
        name='cheese', type='dairy')
    ingredient31 = Ingredient(
        name='provolone', type='dairy')
    ingredient32 = Ingredient(
        name='cheddar', type='dairy')
    ingredient33 = Ingredient(
        name='parmesan', type='dairy')
    ingredient34 = Ingredient(
        name='cream cheese', type='dairy')
    ingredient35 = Ingredient(
        name='brie cheese', type='dairy')
    ingredient36 = Ingredient(
        name='bleu cheese', type='dairy')
    ingredient37 = Ingredient(
        name='heavy cream', type='dairy')
    ingredient38 = Ingredient(
        name='half and half', type='dairy')
    ingredient39 = Ingredient(
        name='whipping cream', type='dairy')
    ingredient40 = Ingredient(
        name='ice cream', type='dairy')
    

    ingredient41 = Ingredient(
        name='steak', type='protein')
    ingredient42 = Ingredient(
        name='chicken', type='protein')
    ingredient43 = Ingredient(
        name='salmon', type='protein')
    ingredient44 = Ingredient(
        name='ground beef', type='protein')
    ingredient45 = Ingredient(
        name='pork belly', type='protein')
    ingredient46 = Ingredient(
        name='pork loin', type='protein')
    ingredient47 = Ingredient(
        name='sausage', type='protein')
    ingredient48 = Ingredient(
        name='sausage (ground)', type='protein')
    ingredient49 = Ingredient(
        name='pepperoni', type='protein')
    ingredient50 = Ingredient(
        name='ham', type='protein')
    ingredient51 = Ingredient(
        name='ham (deli)', type='protein')
    ingredient52 = Ingredient(
        name='bacon', type='protein')
    ingredient53 = Ingredient(
        name='turkey', type='protein')
    ingredient54 = Ingredient(
        name='turkey (deli)', type='protein')
    ingredient55 = Ingredient(
        name='chicken tenders', type='protein')
    ingredient56 = Ingredient(
        name='chicken breasts', type='protein')
    ingredient57 = Ingredient(
        name='chicken thighs', type='protein')
    ingredient58 = Ingredient(
        name='chicken wings', type='protein')
    
    ingredient59 = Ingredient(
        name='asparagus', type='vegetable')
    ingredient60 = Ingredient(
        name='beets', type='vegetable')
    ingredient61 = Ingredient(
        name='broccoli', type='vegetable')
    ingredient62 = Ingredient(
        name='tomatoes', type='vegetable')
    ingredient63 = Ingredient(
        name='cucumbers', type='vegetable')
    ingredient64 = Ingredient(
        name='green beans', type='vegetable')
    ingredient65 = Ingredient(
        name='brussel sprouts', type='vegetable')
    ingredient66 = Ingredient(
        name='cabbage', type='vegetable')
    ingredient67 = Ingredient(
        name='potatoes', type='vegetable')
    ingredient68 = Ingredient(
        name='radishes', type='vegetable')
    ingredient69 = Ingredient(
        name='sweet potatoes', type='vegetable')
    ingredient70 = Ingredient(
        name='carrots', type='vegetable')
    ingredient71 = Ingredient(
        name='corn', type='vegetable')
    ingredient72 = Ingredient(
        name='lettuce', type='vegetable')
    ingredient73 = Ingredient(
        name='spinach', type='vegetable')
    ingredient74 = Ingredient(
        name='mushrooms', type='vegetable')
    ingredient75 = Ingredient(
        name='onions', type='vegetable')
    ingredient76 = Ingredient(
        name='shallots', type='vegetable')
    ingredient77 = Ingredient(
        name='bell peppers', type='vegetable')
    ingredient78 = Ingredient(
        name='jalapenos', type='vegetable')
    ingredient79 = Ingredient(
        name='squash', type='vegetable')
    ingredient80 = Ingredient(
        name='butternut squash', type='vegetable')
    ingredient81 = Ingredient(
        name='zucchini', type='vegetable')
    ingredient82 = Ingredient(
        name='avocado', type='vegetable')
    ingredient83 = Ingredient(
        name='fresno peppers', type='vegetable')
    ingredient84 = Ingredient(
        name='serrano peppers', type='vegetable')


    ingredient85 = Ingredient(
        name='pasta', type='grain')
    ingredient86 = Ingredient(
        name='rigatoni', type='grain')
    ingredient87 = Ingredient(
        name='spaghetti noodles', type='grain')
    ingredient88 = Ingredient(
        name='rice', type='grain')
    ingredient89 = Ingredient(
        name='white rice', type='grain')
    ingredient90 = Ingredient(
        name='brown rice', type='grain')
    ingredient91 = Ingredient(
        name='jasmine rice', type='grain')
    ingredient92 = Ingredient(
        name='risotto', type='grain')
    ingredient93 = Ingredient(
        name='ferro', type='grain')
    ingredient94 = Ingredient(
        name='quinoa', type='grain')

    ingredient95 = Ingredient(
        name='coffee', type='pantry staple')
    ingredient96 = Ingredient(
        name='bread', type='pantry staple')
    ingredient97 = Ingredient(
        name='flour', type='pantry staple')
    ingredient98 = Ingredient(
        name='sugar', type='pantry staple')
    ingredient99 = Ingredient(
        name='baking soda', type='pantry staple')
    ingredient100 = Ingredient(
        name='baking powder', type='pantry staple')
    ingredient101 = Ingredient(
        name='chicken broth', type='pantry staple')
    ingredient102 = Ingredient(
        name='beef broth', type='pantry staple')

    ingredient103 = Ingredient(
        name='butter', type='fat')
    ingredient104 = Ingredient(
        name='olive oil', type='fat')
    ingredient105 = Ingredient(
        name='vegetable oil', type='fat')
    ingredient106 = Ingredient(
        name='avocado oil', type='fat')
    ingredient107 = Ingredient(
        name='coconut oil', type='fat')
    ingredient108 = Ingredient(
        name='peanut oil', type='fat')
    ingredient109 = Ingredient(
        name='sesame oil', type='fat')
    ingredient110 = Ingredient(
        name='peanut', type='fat')
    ingredient111 = Ingredient(
        name='walnut', type='fat')
    ingredient112 = Ingredient(
        name='almond', type='fat')
    ingredient113 = Ingredient(
        name='cashew', type='fat')
    ingredient114 = Ingredient(
        name='brazil nut', type='fat')
    ingredient115 = Ingredient(
        name='pistachio', type='fat')
    ingredient116 = Ingredient(
        name='pecan', type='fat')

    ingredient117 = Ingredient(
        name='salt', type='spice')
    ingredient118 = Ingredient(
        name='pepper', type='spice')
    ingredient119 = Ingredient(
        name='cayenne pepper', type='spice')
    ingredient120 = Ingredient(
        name='cinnamon', type='spice')
    ingredient121 = Ingredient(
        name='cloves', type='spice')
    ingredient122 = Ingredient(
        name='crushed red pepper', type='spice')
    ingredient123 = Ingredient(
        name='dried oregano', type='spice')
    ingredient124 = Ingredient(
        name='dried thyme', type='spice')
    ingredient125 = Ingredient(
        name='cumin', type='spice')
    ingredient126 = Ingredient(
        name='curry powder', type='spice')
    ingredient127 = Ingredient(
        name='garlic powder', type='spice')
    ingredient128 = Ingredient(
        name='ground ginger', type='spice')
    ingredient129 = Ingredient(
        name='dried rosemary', type='spice')

    ingredient130 = Ingredient(
        name='mint', type='herb')
    ingredient131 = Ingredient(
        name='coriander', type='herb')
    ingredient132 = Ingredient(
        name='basil', type='herb')
    ingredient133 = Ingredient(
        name='parsley', type='herb')
    ingredient134 = Ingredient(
        name='chive', type='herb')
    ingredient135 = Ingredient(
        name='dill', type='herb')
    ingredient136 = Ingredient(
        name='thyme', type='herb')
    ingredient137 = Ingredient(
        name='oregano', type='herb')
    ingredient138 = Ingredient(
        name='rosemary', type='herb')
    ingredient139 = Ingredient(
        name='sage', type='herb')
    ingredient140 = Ingredient(
        name='tarragon', type='herb')
    ingredient141 = Ingredient(
        name='bay leaf', type='herb')
    

    
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
    db.session.add(ingredient28)
    db.session.add(ingredient29)
    db.session.add(ingredient30)
    db.session.add(ingredient31)
    db.session.add(ingredient32)
    db.session.add(ingredient33)
    db.session.add(ingredient34)
    db.session.add(ingredient35)
    db.session.add(ingredient36)
    db.session.add(ingredient37)
    db.session.add(ingredient38)
    db.session.add(ingredient39)
    db.session.add(ingredient40)
    db.session.add(ingredient41)
    db.session.add(ingredient42)
    db.session.add(ingredient43)
    db.session.add(ingredient44)
    db.session.add(ingredient45)
    db.session.add(ingredient46)
    db.session.add(ingredient47)
    db.session.add(ingredient48)
    db.session.add(ingredient49)
    db.session.add(ingredient50)
    db.session.add(ingredient51)
    db.session.add(ingredient52)
    db.session.add(ingredient53)
    db.session.add(ingredient54)
    db.session.add(ingredient55)
    db.session.add(ingredient56)
    db.session.add(ingredient57)
    db.session.add(ingredient58)
    db.session.add(ingredient59)
    db.session.add(ingredient60)
    db.session.add(ingredient61)
    db.session.add(ingredient62)
    db.session.add(ingredient63)
    db.session.add(ingredient64)
    db.session.add(ingredient65)
    db.session.add(ingredient66)
    db.session.add(ingredient67)
    db.session.add(ingredient68)
    db.session.add(ingredient69)
    db.session.add(ingredient70)
    db.session.add(ingredient71)
    db.session.add(ingredient72)
    db.session.add(ingredient73)
    db.session.add(ingredient74)
    db.session.add(ingredient75)
    db.session.add(ingredient76)
    db.session.add(ingredient77)
    db.session.add(ingredient78)
    db.session.add(ingredient79)
    db.session.add(ingredient80)
    db.session.add(ingredient81)
    db.session.add(ingredient82)
    db.session.add(ingredient83)
    db.session.add(ingredient84)
    db.session.add(ingredient85)
    db.session.add(ingredient86)
    db.session.add(ingredient87)
    db.session.add(ingredient88)
    db.session.add(ingredient89)
    db.session.add(ingredient90)
    db.session.add(ingredient91)
    db.session.add(ingredient92)
    db.session.add(ingredient93)
    db.session.add(ingredient94)
    db.session.add(ingredient95)
    db.session.add(ingredient96)
    db.session.add(ingredient97)
    db.session.add(ingredient98)
    db.session.add(ingredient99)
    db.session.add(ingredient100)
    db.session.add(ingredient101)
    db.session.add(ingredient102)
    db.session.add(ingredient103)
    db.session.add(ingredient104)
    db.session.add(ingredient105)
    db.session.add(ingredient106)
    db.session.add(ingredient107)
    db.session.add(ingredient108)
    db.session.add(ingredient109)
    db.session.add(ingredient110)
    db.session.add(ingredient111)
    db.session.add(ingredient112)
    db.session.add(ingredient113)
    db.session.add(ingredient114)
    db.session.add(ingredient115)
    db.session.add(ingredient116)
    db.session.add(ingredient117)
    db.session.add(ingredient118)
    db.session.add(ingredient119)
    db.session.add(ingredient120)
    db.session.add(ingredient121)
    db.session.add(ingredient122)
    db.session.add(ingredient123)
    db.session.add(ingredient124)
    db.session.add(ingredient125)
    db.session.add(ingredient126)
    db.session.add(ingredient127)
    db.session.add(ingredient128)
    db.session.add(ingredient129)
    db.session.add(ingredient130)
    db.session.add(ingredient131)
    db.session.add(ingredient132)
    db.session.add(ingredient133)
    db.session.add(ingredient134)
    db.session.add(ingredient135)
    db.session.add(ingredient136)
    db.session.add(ingredient137)
    db.session.add(ingredient138)
    db.session.add(ingredient139)
    db.session.add(ingredient140)
    db.session.add(ingredient141)

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
