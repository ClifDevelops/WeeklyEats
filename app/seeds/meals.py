from app.models import db, Meal, UserMeal


def seed_meals():
    meal1 = Meal(name='Spaghetti with Meat Sauce', cuisine='Italian',
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
    meal3 = Meal(name='Cheeseburgers', cuisine='American', recipe='''1. Preheat a skillet over medium heat. Lightly toast both halves of the hamburger bun, cut sides down, 2 to 3 minutes. Set aside.
    2. Separate beef into 2 portions and form each into a thin patty slightly larger than the bun. Lightly salt each patty and cook on one side for 2 to 3 minutes. Flip patties over and immediately place two slices of American cheese on each one. Cook until meat has reached desired doneness, 2 to 3 minutes more.
    3. Saute any veggies (mushrooms, peppers) and prepare other fresh veggies.
    4. Assemble the double cheeseburger in the following order: bottom bun, dressing, tomato, lettuce, beef patty with cheese, onion, beef patty with cheese, and top bun.
    ''')
    meal4 = Meal(name='Salmon and Roasted Vegetables', cuisine='French', recipe='''1. Set an oven rack about 6 inches from the heat source and preheat the oven's broiler. Line a baking pan with aluminum foil.
    2. Pour oil into a medium bowl. Rinse salmon fillets and pat dry. Dip fillets into oil, being sure to coat both sides, and place skin-side down into the prepared baking pan. Squeeze as much juice as you can from 1 lemon half over the fillets. Coat both sides of salmon with parsley, oregano, basil, and garlic, and sprinkle with 1/2 of the kosher salt.
    3. Place under the preheated broiler and cook until center is light pink and edges are golden brown, 10 to 15 minutes.
    4. Remove fillets from the oven and immediately plate. Squeeze remaining lemon half over top and sprinkle with remaining kosher salt. Serve with lemon slices. 
    ''')
    meal5 = Meal(name='Chicken Tacos', cuisine='Mexican', recipe='''1. Mix water and taco seasoning in a large bowl. Add tomato sauce, vinegar, garlic, oregano, cumin, and sugar; mix well.
    2. Heat oil in a large skillet over medium-high heat. Add chicken and cook until golden brown, about 5 minutes per side. Add tomato sauce mixture and bring to a boil. Reduce heat to medium-low, cover, and simmer until chicken is no longer pink in the center and the juices run clear, about 20 minutes. An instant-read thermometer inserted into the center should read at least 165 degrees F (74 degrees C).
    3. Remove chicken breasts from the pan and shred meat with 2 forks when cool enough to handle. Return shredded chicken to the pan with the tomato sauce. Cook and stir until chicken is coated with sauce and sauce reduces a bit, about 5 minutes.
    4. Transfer chicken and sauce to a serving bowl and spoon onto taco shells.
    ''')
    meal6 = Meal(name='Roast Chicken with Potatoes', cuisine='French',
                 recipe='''1. Preheat oven to 400 degrees F (200 degrees C). Blend butter with ginger, lemon zest, cumin, garlic, salt, and pepper until well combined; set aside.
    2. Prepare the potatoes, either boiled and mashed or cut into a large dice and roasted with herbs and spices.
    3. Melt 3 tablespoons butter mixture; toss with potatoes, carrots, parsnips, and green onions. Scatter around chicken.
    4. Carefully loosen skin over breast meat, legs, and thighs using fingertips. Spread remaining butter mixture evenly under and over skin of chicken.
    5. Roast, basting occasionally, for 60 to 75 minutes (or until an instant-read thermometer registers 165 degrees F/74 degrees C in thigh and breast meat).
    6. Cover and rest for 10 minutes. Carve chicken into portions and serve with vegetables.
    ''')
    meal7 = Meal(name='Flank Steak Tacos', cuisine='Mexican',
                 recipe='''1. Combine onion, cilantro, lime juice, soy sauce, olive oil, brown sugar, oregano, red pepper flakes, and garlic in a large bowl.
    2. Place steak in a baking pan and pour marinade on top. Cover and refrigerate at least 1 to 4 hours.
    3. Grill steak 2 to 4 minutes per side, to desired doneness. Allow meat to rest 5 to 10 minutes before slicing against the grain into 1/4-inch slices.
    4. Add meat to tortillas and top with your favorite toppings.
    ''')
    


    db.session.add(meal1)
    db.session.add(meal2)
    db.session.add(meal3)
    db.session.add(meal4)
    db.session.add(meal5)
    db.session.add(meal6)
    db.session.add(meal7)

    db.session.commit()

def undo_meals():
    db.session.execute('TRUNCATE meals RESTART IDENTITY CASCADE;')
    db.session.commit()


def seed_user_meals():
    user_meal1 = UserMeal(user_id=1, meal_id=1)
    user_meal2 = UserMeal(user_id=1, meal_id=2)
    user_meal3 = UserMeal(user_id=1, meal_id=3)
    user_meal4 = UserMeal(user_id=1, meal_id=4)
    user_meal5 = UserMeal(user_id=1, meal_id=5)
    user_meal6 = UserMeal(user_id=1, meal_id=6)
    user_meal7 = UserMeal(user_id=1, meal_id=7)

    db.session.add(user_meal1)
    db.session.add(user_meal2)
    db.session.add(user_meal3)
    db.session.add(user_meal4)
    db.session.add(user_meal5)
    db.session.add(user_meal6)
    db.session.add(user_meal7)

    db.session.commit()


def undo_user_meals():
    db.session.execute('TRUNCATE user_meals RESTART IDENTITY CASCADE;')
    db.session.commit()
