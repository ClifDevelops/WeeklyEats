import React from "react";
import { useEffect, useState } from "react";
import { useParams, useHistory, NavLink } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getAllMeals } from "../../store/meal";
import { deleteFromGroceryList, addToGroceryList } from "../../store/grocerylist";
import { getAllIngredients } from "../../store/ingredient";
import MealIngredientsForm from "../MealIngredientsForm";
import './MealDisplay.css'
import IngredientForm from "../IngredientForm";

const MealDisplay = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const { mealId } = useParams();
    const meal = useSelector(state => state?.meal[mealId])
    const ingredients = useSelector((state) => state?.ingredient?.ingredients);
    // console.log('HERE IT IS', meal?.meal_ingredients.forEach(ingredient => ingredient.ingredient['name']))
    // console.log("THE NEXT ONE", meal?.meal_ingredients[0].ingredient.name);

     useEffect(() => {
       dispatch(getAllMeals());
     }, []);

    // useEffect(() => {
    //     dispatch(getAllIngredients())
    // }, [])

    if (!meal){
        history.push('/meals')
    }
    return (
      <div>
        <div className="meal-display-container">
          <div className='meal-container'>
            <div className='meal-display-name'>{meal?.name}</div>
            <div className='meal-display-cuisine'>Cuisine: {meal?.cuisine}</div>
            <div className='meal-display-recipe-title'> RECIPE</div>
            <div className='meal-display-recipe'>{meal?.recipe}</div>
            <NavLink to={`/meals/${mealId}/edit`}>
              <button className='meal-edit-button'> Edit Meal</button>
            </NavLink>
          </div>
          <div className='meal-display-ingredients-container'>
            <div>INGREDIENTS</div>
            {/* <div>{meal?.meal_ingredients[0].ingredient.name}</div> */}
            <div>{meal?.meal_ingredients.map((ingredient) => {
                return (
                    <div>{ingredient.ingredient.name}</div>
                )})}</div>
            <MealIngredientsForm mealId={mealId} />
            <IngredientForm />
          </div>
        </div>
      </div>
    );
}

export default MealDisplay