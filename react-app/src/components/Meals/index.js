import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllMeals } from "../../store/meal";
import { addMealIngredientsToGroceryList } from "../../store/grocerylist"
import "./Meals.css";

const Meals = () => {
    const dispatch = useDispatch()
    const meals = useSelector(state => state?.meal)
    // console.log(meals)

    useEffect(() => {
        dispatch(getAllMeals())
    }, []);

    if (Object.values(meals).length){
        return (
            <div className='all-meals-container'>
                {Object.values(meals).map((meal) => {
                    return (
                    <div key={meal.id} className="meal-individual-card">
                        {/* {console.log(meal.id)} */}
                        <div><NavLink to={`/meals/${meal.id}`} className='meal-navlink'>{meal.name}</NavLink></div>
                        <div className='meal-card-cuisine'>{meal.cuisine}</div>
                        {/* <div className='meal-recipe'>{meal.recipe}</div> */}
                        { meal.meal_ingredients.length ?
                            <button className='meal-card-button' onClick={() => dispatch(addMealIngredientsToGroceryList(meal.meal_ingredients))}>Add to Grocery List</button>
                            : ""
                            }
                    </div>
                    );
                    })} 
            </div>
            
        )} else {
            return (
                <div className='no-meals-to-display-text-container'>
                    Haven't added a meal yet? Get started <NavLink className='no-meals-to-display-link' to='/meals/create'>here!</NavLink>
                </div>
            )
        }
}

export default Meals