import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { addToMeals } from "../../store/meal";
import "./MealForm.css";

const MealForm = () => {
    const dispatch = useDispatch();
    const [name, setName] = useState('');
    const [cuisine, setCuisine] = useState('');
    const [recipe, setRecipe] = useState('');

    const updateName = (e) => {
        setName(e.target.value)
    }

    const updateCuisine = (e) => {
      setCuisine(e.target.value);
    };

    const updateRecipe = (e) => {
      setRecipe(e.target.value);
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        const meal = {
            name,
            cuisine,
            recipe,
        };
        dispatch(addToMeals(meal));
        setName('');
        setCuisine('');
        setRecipe('');
    };


    return (
      <form onSubmit={onSubmit}>
        <div>
          <input
            type="text"
            name="name"
            onChange={updateName}
            value={name}
            placeholder="Meal Name"
          ></input>
        </div>
        <div>
          <input
            type="text"
            name="cuisine"
            onChange={updateCuisine}
            value={cuisine}
            placeholder="Cuisine"
          ></input>
        </div>
        <div>
          <textarea
            type="text"
            name="recipe"
            onChange={updateRecipe}
            value={recipe}
            placeholder="Recipe goes here!"
          ></textarea>
        </div>
        <button type="submit">Create a Meal</button>
      </form>
    );


}

export default MealForm;
