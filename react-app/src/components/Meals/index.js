import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllMeals } from "../../store/meal";
import "./Meals.css";

const Meals = () => {
    const dispatch = useDispatch()
    const meals = useSelector(state => state?.meal)
    // console.log(meals)

    useEffect(() => {
        dispatch(getAllMeals())
    }, []);


    return (
        <div className='all-meals-container'>
            {Object.values(meals).map((meal) => {
                return (
                  <div key={meal.id} className="meal-individual-card">
                      {/* {console.log(meal.id)} */}
                    <div><NavLink to={`/meals/${meal.id}`}>{meal.name}</NavLink></div>
                    <div>{meal.cuisine}</div>
                    <div className='meal-recipe'>{meal.recipe}</div>
                    <button>Add to Grocery List</button>
                    <button>Add ingredients to meal</button>
                  </div>
                );


                })}
             
        </div>
    )
}

export default Meals