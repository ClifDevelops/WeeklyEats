import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllMeals } from "../../store/meal";
import {
  addMealIngredientsToGroceryList,
  removeMealIngredientsFromGroceryList,
} from "../../store/grocerylist";
import "./Meals.css";

const Meals = () => {
    const dispatch = useDispatch()
    const meals = useSelector(state => state?.meal)
    const mealsInGL = useSelector(state => state?.groceryList?.mealsInGL)
    const [searchTerm, setSearchTerm] = useState("");

   
    const addToGL = async (meal) => {
        await dispatch(addMealIngredientsToGroceryList(meal));
        await dispatch(getAllMeals());
    }

    const removeFromGL = async (meal) => {
        await dispatch(removeMealIngredientsFromGroceryList(meal));
        await dispatch(getAllMeals());
    }

    useEffect(() => {
        dispatch(getAllMeals())
    }, []);

    if (Object.values(meals).length){
        return (
          <div className="all-meals-container">
            <input
              className="meals-search-input"
              type="text"
              placeholder="Filter your meals"
              onChange={(e) => {
                setSearchTerm(e.target.value);
              }}
            />
            {Object.values(meals)
              .filter((meal) => {
                if (searchTerm === "") {
                  return meal;
                } else if (
                  meal?.name
                    .toLowerCase()
                    .includes(searchTerm.toLowerCase()) ||
                  meal?.cuisine
                    .toLowerCase()
                    .includes(searchTerm.toLowerCase())
                ) {
                  return meal;
                }
              })
              .map((meal) => {
                return (
                  <div key={meal.id} className="meal-individual-card">
                    <div>
                      <NavLink
                        to={`/meals/${meal.id}`}
                        className="meal-navlink"
                      >
                        {meal.name}
                      </NavLink>
                    </div>
                    <div className="meal-card-cuisine">{meal.cuisine}</div>

                    {mealsInGL.includes(meal.id) ? (
                      <button
                        className="meal-card-remove-button"
                        onClick={() => removeFromGL(meal)}
                      >
                        Remove from Grocery List
                      </button>
                    ) : meal.meal_ingredients.length ? (
                      <button
                        className="meal-card-add-button"
                        onClick={() => addToGL(meal)}
                      >
                        Add to Grocery List
                      </button>
                    ) : (
                      ""
                    )}
                  </div>
                );
              })}
          </div>
        );} else {
            return (
                <div className='no-meals-to-display-text-container'>
                    Haven't added a meal yet? Get started <NavLink className='no-meals-to-display-link' to='/meals/create'>here!</NavLink>
                </div>
            )
        }
}

export default Meals