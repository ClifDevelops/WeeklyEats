from app.models import db, Ingredient, MealIngredient

def seed_ingredients():
    ingredient1 = Ingredient(
        name='apples', type='fruit', editable=False)
    ingredient2 = Ingredient(
        name='oranges', type='fruit', editable=False)
    ingredient3 = Ingredient(
        name='bananas', type='fruit', editable=False)
    ingredient4 = Ingredient(
        name='blueberries', type='fruit', editable=False)
    ingredient5 = Ingredient(
        name='raspberries', type='fruit', editable=False)
    ingredient6 = Ingredient(
        name='coconuts', type='fruit', editable=False)
    ingredient7 = Ingredient(
        name='cantaloupes', type='fruit', editable=False)
    ingredient8 = Ingredient(
        name='cherries', type='fruit', editable=False)
    ingredient9 = Ingredient(
        name='blackberries', type='fruit', editable=False)
    ingredient10 = Ingredient(
        name='kiwis', type='fruit', editable=False)
    ingredient11 = Ingredient(
        name='plums', type='fruit', editable=False)
    ingredient12 = Ingredient(
        name='grapes', type='fruit', editable=False)
    ingredient13 = Ingredient(
        name='lemons', type='fruit', editable=False)
    ingredient14 = Ingredient(
        name='limes', type='fruit', editable=False)
    ingredient15 = Ingredient(
        name='grapefruits', type='fruit', editable=False)
    ingredient16 = Ingredient(
        name='mangoes', type='fruit', editable=False)
    ingredient17 = Ingredient(
        name='peaches', type='fruit', editable=False)
    ingredient18 = Ingredient(
        name='tangerines', type='fruit', editable=False)
    ingredient19 = Ingredient(
        name='pears', type='fruit', editable=False)
    ingredient20 = Ingredient(
        name='pineapple', type='fruit', editable=False)
    ingredient21 = Ingredient(
        name='pomegranate', type='fruit', editable=False)
    ingredient22 = Ingredient(
        name='strawberries', type='fruit', editable=False)
    ingredient23 = Ingredient(
        name='watermelon', type='fruit', editable=False)


    ingredient24 = Ingredient(
        name='eggs', type='dairy', editable=False)
    ingredient25 = Ingredient(
        name='whole milk', type='dairy', editable=False)
    ingredient26 = Ingredient(
        name='oat milk', type='dairy', editable=False)
    ingredient27 = Ingredient(
        name='almond milk', type='dairy', editable=False)
    ingredient28 = Ingredient(
        name='yogurt', type='dairy', editable=False)
    ingredient29 = Ingredient(
        name='sour cream', type='dairy', editable=False)
    ingredient30 = Ingredient(
        name='cheese', type='dairy', editable=False)
    ingredient31 = Ingredient(
        name='provolone', type='dairy', editable=False)
    ingredient32 = Ingredient(
        name='cheddar', type='dairy', editable=False)
    ingredient33 = Ingredient(
        name='parmesan', type='dairy', editable=False)
    ingredient34 = Ingredient(
        name='cream cheese', type='dairy', editable=False)
    ingredient35 = Ingredient(
        name='brie cheese', type='dairy', editable=False)
    ingredient36 = Ingredient(
        name='bleu cheese', type='dairy', editable=False)
    ingredient37 = Ingredient(
        name='heavy cream', type='dairy', editable=False)
    ingredient38 = Ingredient(
        name='half and half', type='dairy', editable=False)
    ingredient39 = Ingredient(
        name='whipping cream', type='dairy', editable=False)
    ingredient40 = Ingredient(
        name='ice cream', type='dairy', editable=False)
    

    ingredient41 = Ingredient(
        name='steak', type='protein', editable=False)
    ingredient42 = Ingredient(
        name='chicken', type='protein', editable=False)
    ingredient43 = Ingredient(
        name='salmon', type='protein', editable=False)
    ingredient44 = Ingredient(
        name='ground beef', type='protein', editable=False)
    ingredient45 = Ingredient(
        name='pork belly', type='protein', editable=False)
    ingredient46 = Ingredient(
        name='pork loin', type='protein', editable=False)
    ingredient47 = Ingredient(
        name='sausage', type='protein', editable=False)
    ingredient48 = Ingredient(
        name='sausage (ground)', type='protein', editable=False)
    ingredient49 = Ingredient(
        name='pepperoni', type='protein', editable=False)
    ingredient50 = Ingredient(
        name='ham', type='protein', editable=False)
    ingredient51 = Ingredient(
        name='ham (deli)', type='protein', editable=False)
    ingredient52 = Ingredient(
        name='bacon', type='protein', editable=False)
    ingredient53 = Ingredient(
        name='turkey', type='protein', editable=False)
    ingredient54 = Ingredient(
        name='turkey (deli)', type='protein', editable=False)
    ingredient55 = Ingredient(
        name='chicken tenders', type='protein', editable=False)
    ingredient56 = Ingredient(
        name='chicken breasts', type='protein', editable=False)
    ingredient57 = Ingredient(
        name='chicken thighs', type='protein', editable=False)
    ingredient58 = Ingredient(
        name='chicken wings', type='protein', editable=False)
    
    ingredient59 = Ingredient(
        name='asparagus', type='vegetable', editable=False)
    ingredient60 = Ingredient(
        name='beets', type='vegetable', editable=False)
    ingredient61 = Ingredient(
        name='broccoli', type='vegetable', editable=False)
    ingredient62 = Ingredient(
        name='tomatoes', type='vegetable', editable=False)
    ingredient63 = Ingredient(
        name='cucumbers', type='vegetable', editable=False)
    ingredient64 = Ingredient(
        name='green beans', type='vegetable', editable=False)
    ingredient65 = Ingredient(
        name='brussel sprouts', type='vegetable', editable=False)
    ingredient66 = Ingredient(
        name='cabbage', type='vegetable', editable=False)
    ingredient67 = Ingredient(
        name='potatoes', type='vegetable', editable=False)
    ingredient68 = Ingredient(
        name='radishes', type='vegetable', editable=False)
    ingredient69 = Ingredient(
        name='sweet potatoes', type='vegetable', editable=False)
    ingredient70 = Ingredient(
        name='carrots', type='vegetable', editable=False)
    ingredient71 = Ingredient(
        name='corn', type='vegetable', editable=False)
    ingredient72 = Ingredient(
        name='lettuce', type='vegetable', editable=False)
    ingredient73 = Ingredient(
        name='spinach', type='vegetable', editable=False)
    ingredient74 = Ingredient(
        name='mushrooms', type='vegetable', editable=False)
    ingredient75 = Ingredient(
        name='onions', type='vegetable', editable=False)
    ingredient76 = Ingredient(
        name='shallots', type='vegetable', editable=False)
    ingredient77 = Ingredient(
        name='bell peppers', type='vegetable', editable=False)
    ingredient78 = Ingredient(
        name='jalapenos', type='vegetable', editable=False)
    ingredient79 = Ingredient(
        name='squash', type='vegetable', editable=False)
    ingredient80 = Ingredient(
        name='butternut squash', type='vegetable', editable=False)
    ingredient81 = Ingredient(
        name='zucchini', type='vegetable', editable=False)
    ingredient82 = Ingredient(
        name='avocado', type='vegetable', editable=False)
    ingredient83 = Ingredient(
        name='fresno peppers', type='vegetable', editable=False)
    ingredient84 = Ingredient(
        name='serrano peppers', type='vegetable', editable=False)


    ingredient85 = Ingredient(
        name='pasta', type='grain', editable=False)
    ingredient86 = Ingredient(
        name='rigatoni', type='grain', editable=False)
    ingredient87 = Ingredient(
        name='spaghetti noodles', type='grain', editable=False)
    ingredient88 = Ingredient(
        name='rice', type='grain', editable=False)
    ingredient89 = Ingredient(
        name='white rice', type='grain', editable=False)
    ingredient90 = Ingredient(
        name='brown rice', type='grain', editable=False)
    ingredient91 = Ingredient(
        name='jasmine rice', type='grain', editable=False)
    ingredient92 = Ingredient(
        name='risotto', type='grain', editable=False)
    ingredient93 = Ingredient(
        name='ferro', type='grain', editable=False)
    ingredient94 = Ingredient(
        name='quinoa', type='grain', editable=False)

    ingredient95 = Ingredient(
        name='coffee', type='pantry staple', editable=False)
    ingredient96 = Ingredient(
        name='bread', type='pantry staple', editable=False)
    ingredient97 = Ingredient(
        name='flour', type='pantry staple', editable=False)
    ingredient98 = Ingredient(
        name='sugar', type='pantry staple', editable=False)
    ingredient99 = Ingredient(
        name='baking soda', type='pantry staple', editable=False)
    ingredient100 = Ingredient(
        name='baking powder', type='pantry staple', editable=False)
    ingredient101 = Ingredient(
        name='chicken broth', type='pantry staple', editable=False)
    ingredient102 = Ingredient(
        name='beef broth', type='pantry staple', editable=False)

    ingredient103 = Ingredient(
        name='butter', type='fat', editable=False)
    ingredient104 = Ingredient(
        name='olive oil', type='fat', editable=False)
    ingredient105 = Ingredient(
        name='vegetable oil', type='fat', editable=False)
    ingredient106 = Ingredient(
        name='avocado oil', type='fat', editable=False)
    ingredient107 = Ingredient(
        name='coconut oil', type='fat', editable=False)
    ingredient108 = Ingredient(
        name='peanut oil', type='fat', editable=False)
    ingredient109 = Ingredient(
        name='sesame oil', type='fat', editable=False)
    ingredient110 = Ingredient(
        name='peanut', type='fat', editable=False)
    ingredient111 = Ingredient(
        name='walnut', type='fat', editable=False)
    ingredient112 = Ingredient(
        name='almond', type='fat', editable=False)
    ingredient113 = Ingredient(
        name='cashew', type='fat', editable=False)
    ingredient114 = Ingredient(
        name='brazil nut', type='fat', editable=False)
    ingredient115 = Ingredient(
        name='pistachio', type='fat', editable=False)
    ingredient116 = Ingredient(
        name='pecan', type='fat', editable=False)

    ingredient117 = Ingredient(
        name='salt', type='spice', editable=False)
    ingredient118 = Ingredient(
        name='pepper', type='spice', editable=False)
    ingredient119 = Ingredient(
        name='cayenne pepper', type='spice', editable=False)
    ingredient120 = Ingredient(
        name='cinnamon', type='spice', editable=False)
    ingredient121 = Ingredient(
        name='cloves', type='spice', editable=False)
    ingredient122 = Ingredient(
        name='crushed red pepper', type='spice', editable=False)
    ingredient123 = Ingredient(
        name='dried oregano', type='spice', editable=False)
    ingredient124 = Ingredient(
        name='dried thyme', type='spice', editable=False)
    ingredient125 = Ingredient(
        name='cumin', type='spice', editable=False)
    ingredient126 = Ingredient(
        name='curry powder', type='spice', editable=False)
    ingredient127 = Ingredient(
        name='garlic powder', type='spice', editable=False)
    ingredient128 = Ingredient(
        name='ground ginger', type='spice', editable=False)
    ingredient129 = Ingredient(
        name='dried rosemary', type='spice', editable=False)

    ingredient130 = Ingredient(
        name='mint', type='herb', editable=False)
    ingredient131 = Ingredient(
        name='coriander', type='herb', editable=False)
    ingredient132 = Ingredient(
        name='basil', type='herb', editable=False)
    ingredient133 = Ingredient(
        name='parsley', type='herb', editable=False)
    ingredient134 = Ingredient(
        name='chive', type='herb', editable=False)
    ingredient135 = Ingredient(
        name='dill', type='herb', editable=False)
    ingredient136 = Ingredient(
        name='thyme', type='herb', editable=False)
    ingredient137 = Ingredient(
        name='oregano', type='herb', editable=False)
    ingredient138 = Ingredient(
        name='rosemary', type='herb', editable=False)
    ingredient139 = Ingredient(
        name='sage', type='herb', editable=False)
    ingredient140 = Ingredient(
        name='tarragon', type='herb', editable=False)
    ingredient141 = Ingredient(
        name='bay leaf', type='herb', editable=False)

    ingredient142 = Ingredient(
        name='burger buns', type='grain', editable=False)
    ingredient143 = Ingredient(
        name='garlic', type='vegetable', editable=False)
    ingredient144 = Ingredient(
        name='tomato sauce', type='pantry staple', editable=False)
    ingredient145 = Ingredient(
        name='tomato paste', type='pantry staple', editable=False)
    ingredient146 = Ingredient(
        name='taco seasoning', type='spice', editable=False)
    ingredient147 = Ingredient(
        name='taco shells', type='grain', editable=False)
    ingredient148 = Ingredient(
        name='tortillas', type='grain', editable=False)
    ingredient149 = Ingredient(
        name='parsnips', type='vegetable', editable=False)
    ingredient150 = Ingredient(
        name='green onion', type='vegetable', editable=False)
    ingredient151 = Ingredient(
        name='ginger', type='vegetable', editable=False)
    ingredient152 = Ingredient(
        name='brown sugar', type='pantry staple', editable=False)
    ingredient153 = Ingredient(
        name='soy sauce', type='pantry staple', editable=False)
    ingredient154 = Ingredient(
        name='cilantro', type='herb', editable=False)
    ingredient155 = Ingredient(
        name='flank steak', type='protein', editable=False)
    
    

    
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
    db.session.add(ingredient142)
    db.session.add(ingredient143)
    db.session.add(ingredient144)
    db.session.add(ingredient145)
    db.session.add(ingredient146)
    db.session.add(ingredient147)
    db.session.add(ingredient148)
    db.session.add(ingredient149)
    db.session.add(ingredient150)
    db.session.add(ingredient151)
    db.session.add(ingredient152)
    db.session.add(ingredient153)
    db.session.add(ingredient154)
    db.session.add(ingredient155)

    db.session.commit()

def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
    

def seed_meal_ingredients():
    meal_ingredient1 = MealIngredient(meal_id=3, ingredient_id=32)
    meal_ingredient2 = MealIngredient(meal_id=3, ingredient_id=33)
    meal_ingredient3 = MealIngredient(meal_id=3, ingredient_id=44)
    meal_ingredient4 = MealIngredient(meal_id=3, ingredient_id=62)
    meal_ingredient5 = MealIngredient(meal_id=3, ingredient_id=72)
    meal_ingredient6 = MealIngredient(meal_id=3, ingredient_id=73)
    meal_ingredient7 = MealIngredient(meal_id=3, ingredient_id=74)
    meal_ingredient8 = MealIngredient(meal_id=3, ingredient_id=75)
    meal_ingredient9 = MealIngredient(meal_id=3, ingredient_id=78)
    meal_ingredient10 = MealIngredient(meal_id=3, ingredient_id=117)
    meal_ingredient11 = MealIngredient(meal_id=3, ingredient_id=127)
    meal_ingredient12 = MealIngredient(meal_id=3, ingredient_id=142)

    meal_ingredient13 = MealIngredient(meal_id=2, ingredient_id=41)
    meal_ingredient14 = MealIngredient(meal_id=2, ingredient_id=59)
    meal_ingredient15 = MealIngredient(meal_id=2, ingredient_id=61)
    meal_ingredient16 = MealIngredient(meal_id=2, ingredient_id=64)
    meal_ingredient17 = MealIngredient(meal_id=2, ingredient_id=67)
    meal_ingredient18 = MealIngredient(meal_id=2, ingredient_id=103)
    meal_ingredient19 = MealIngredient(meal_id=2, ingredient_id=117)
    meal_ingredient20 = MealIngredient(meal_id=2, ingredient_id=118)
    meal_ingredient21 = MealIngredient(meal_id=2, ingredient_id=138)

    meal_ingredient22 = MealIngredient(meal_id=4, ingredient_id=43)
    meal_ingredient23 = MealIngredient(meal_id=4, ingredient_id=104)
    meal_ingredient24 = MealIngredient(meal_id=4, ingredient_id=13)
    meal_ingredient25 = MealIngredient(meal_id=4, ingredient_id=133)
    meal_ingredient26 = MealIngredient(meal_id=4, ingredient_id=123)
    meal_ingredient27 = MealIngredient(meal_id=4, ingredient_id=132)
    meal_ingredient28 = MealIngredient(meal_id=4, ingredient_id=143)
    meal_ingredient29 = MealIngredient(meal_id=4, ingredient_id=117)
    meal_ingredient30 = MealIngredient(meal_id=4, ingredient_id=59)
    meal_ingredient31 = MealIngredient(meal_id=4, ingredient_id=61)

    meal_ingredient32 = MealIngredient(meal_id=1, ingredient_id=33)
    meal_ingredient33 = MealIngredient(meal_id=1, ingredient_id=44)
    meal_ingredient34 = MealIngredient(meal_id=1, ingredient_id=62)
    meal_ingredient35 = MealIngredient(meal_id=1, ingredient_id=87)
    meal_ingredient36 = MealIngredient(meal_id=1, ingredient_id=104)
    meal_ingredient37 = MealIngredient(meal_id=1, ingredient_id=118)
    meal_ingredient38 = MealIngredient(meal_id=1, ingredient_id=127)
    meal_ingredient39 = MealIngredient(meal_id=1, ingredient_id=132)
    meal_ingredient40 = MealIngredient(meal_id=1, ingredient_id=137)
    meal_ingredient41 = MealIngredient(meal_id=1, ingredient_id=143)
    meal_ingredient42 = MealIngredient(meal_id=1, ingredient_id=144)
    meal_ingredient43 = MealIngredient(meal_id=1, ingredient_id=145)

    meal_ingredient44 = MealIngredient(meal_id=5, ingredient_id=14)
    meal_ingredient45 = MealIngredient(meal_id=5, ingredient_id=29)
    meal_ingredient46 = MealIngredient(meal_id=5, ingredient_id=30)
    meal_ingredient47 = MealIngredient(meal_id=5, ingredient_id=56)
    meal_ingredient48 = MealIngredient(meal_id=5, ingredient_id=62)
    meal_ingredient49 = MealIngredient(meal_id=5, ingredient_id=72)
    meal_ingredient50 = MealIngredient(meal_id=5, ingredient_id=75)
    meal_ingredient51 = MealIngredient(meal_id=5, ingredient_id=78)
    meal_ingredient52 = MealIngredient(meal_id=5, ingredient_id=82)
    meal_ingredient53 = MealIngredient(meal_id=5, ingredient_id=143)
    meal_ingredient54 = MealIngredient(meal_id=5, ingredient_id=144)
    meal_ingredient55 = MealIngredient(meal_id=5, ingredient_id=146)
    meal_ingredient56 = MealIngredient(meal_id=5, ingredient_id=147)

    meal_ingredient57 = MealIngredient(meal_id=6, ingredient_id=42)
    meal_ingredient58 = MealIngredient(meal_id=6, ingredient_id=67)
    meal_ingredient59 = MealIngredient(meal_id=6, ingredient_id=70)
    meal_ingredient60 = MealIngredient(meal_id=6, ingredient_id=103)
    meal_ingredient61 = MealIngredient(meal_id=6, ingredient_id=125)
    meal_ingredient62 = MealIngredient(meal_id=6, ingredient_id=117)
    meal_ingredient63 = MealIngredient(meal_id=6, ingredient_id=118)
    meal_ingredient64 = MealIngredient(meal_id=6, ingredient_id=13)
    meal_ingredient65 = MealIngredient(meal_id=6, ingredient_id=149)
    meal_ingredient66 = MealIngredient(meal_id=6, ingredient_id=150)
    meal_ingredient67 = MealIngredient(meal_id=6, ingredient_id=151)
    
    meal_ingredient68 = MealIngredient(meal_id=7, ingredient_id=155)
    meal_ingredient69 = MealIngredient(meal_id=7, ingredient_id=154)
    meal_ingredient70 = MealIngredient(meal_id=7, ingredient_id=153)
    meal_ingredient71 = MealIngredient(meal_id=7, ingredient_id=152)
    meal_ingredient72 = MealIngredient(meal_id=7, ingredient_id=150)
    meal_ingredient73 = MealIngredient(meal_id=7, ingredient_id=148)
    meal_ingredient74 = MealIngredient(meal_id=7, ingredient_id=143)
    meal_ingredient75 = MealIngredient(meal_id=7, ingredient_id=137)
    meal_ingredient76 = MealIngredient(meal_id=7, ingredient_id=122)
    meal_ingredient77 = MealIngredient(meal_id=7, ingredient_id=118)
    meal_ingredient78 = MealIngredient(meal_id=7, ingredient_id=117)
    meal_ingredient79 = MealIngredient(meal_id=7, ingredient_id=78)
    meal_ingredient80 = MealIngredient(meal_id=7, ingredient_id=82)
    meal_ingredient81 = MealIngredient(meal_id=7, ingredient_id=77)
    meal_ingredient82 = MealIngredient(meal_id=7, ingredient_id=29)
    meal_ingredient83 = MealIngredient(meal_id=7, ingredient_id=14)

    
    
    db.session.add(meal_ingredient1)
    db.session.add(meal_ingredient2)
    db.session.add(meal_ingredient3)
    db.session.add(meal_ingredient4)
    db.session.add(meal_ingredient5)
    db.session.add(meal_ingredient6)
    db.session.add(meal_ingredient7)
    db.session.add(meal_ingredient8)
    db.session.add(meal_ingredient9)
    db.session.add(meal_ingredient10)
    db.session.add(meal_ingredient11)
    db.session.add(meal_ingredient12)
    db.session.add(meal_ingredient13)
    db.session.add(meal_ingredient14)
    db.session.add(meal_ingredient15)
    db.session.add(meal_ingredient16)
    db.session.add(meal_ingredient17)
    db.session.add(meal_ingredient18)
    db.session.add(meal_ingredient19)
    db.session.add(meal_ingredient20)
    db.session.add(meal_ingredient21)
    db.session.add(meal_ingredient22)
    db.session.add(meal_ingredient23)
    db.session.add(meal_ingredient24)
    db.session.add(meal_ingredient25)
    db.session.add(meal_ingredient26)
    db.session.add(meal_ingredient27)
    db.session.add(meal_ingredient28)
    db.session.add(meal_ingredient29)
    db.session.add(meal_ingredient30)
    db.session.add(meal_ingredient31)
    db.session.add(meal_ingredient32)
    db.session.add(meal_ingredient33)
    db.session.add(meal_ingredient34)
    db.session.add(meal_ingredient35)
    db.session.add(meal_ingredient36)
    db.session.add(meal_ingredient37)
    db.session.add(meal_ingredient38)
    db.session.add(meal_ingredient39)
    db.session.add(meal_ingredient40)
    db.session.add(meal_ingredient41)
    db.session.add(meal_ingredient42)
    db.session.add(meal_ingredient43)
    db.session.add(meal_ingredient44)
    db.session.add(meal_ingredient45)
    db.session.add(meal_ingredient46)
    db.session.add(meal_ingredient47)
    db.session.add(meal_ingredient48)
    db.session.add(meal_ingredient49)
    db.session.add(meal_ingredient50)
    db.session.add(meal_ingredient51)
    db.session.add(meal_ingredient52)
    db.session.add(meal_ingredient53)
    db.session.add(meal_ingredient54)
    db.session.add(meal_ingredient55)
    db.session.add(meal_ingredient56)
    db.session.add(meal_ingredient57)
    db.session.add(meal_ingredient58)
    db.session.add(meal_ingredient59)
    db.session.add(meal_ingredient60)
    db.session.add(meal_ingredient61)
    db.session.add(meal_ingredient62)
    db.session.add(meal_ingredient63)
    db.session.add(meal_ingredient64)
    db.session.add(meal_ingredient65)
    db.session.add(meal_ingredient66)
    db.session.add(meal_ingredient67)
    db.session.add(meal_ingredient68)
    db.session.add(meal_ingredient69)
    db.session.add(meal_ingredient70)
    db.session.add(meal_ingredient71)
    db.session.add(meal_ingredient72)
    db.session.add(meal_ingredient73)
    db.session.add(meal_ingredient74)
    db.session.add(meal_ingredient75)
    db.session.add(meal_ingredient76)
    db.session.add(meal_ingredient77)
    db.session.add(meal_ingredient78)
    db.session.add(meal_ingredient79)
    db.session.add(meal_ingredient80)
    db.session.add(meal_ingredient81)
    db.session.add(meal_ingredient82)
    db.session.add(meal_ingredient83)
    



    db.session.commit()


def undo_meal_ingredients():
    db.session.execute('TRUNCATE meal_ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
