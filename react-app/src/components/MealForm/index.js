import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { addToMeals } from "../../store/meal";
import "./MealForm.css";

const MealForm = () => {
    const dispatch = useDispatch();
    const [name, setName] = useState('');
    const [cuisine, setCuisine] = useState('American');
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
        setCuisine('American');
        setRecipe('');
        return <Redirect to='/meals' />
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
          <select name="cuisine" onChange={updateCuisine} value={cuisine}>
            <option value="American">American</option>
            <option value="British">British</option>
            <option value="Cajun">Cajun</option>
            <option value="Chinese">Chinese</option>
            <option value="French">French</option>
            <option value="Greek">Greek</option>
            <option value="Indian">Indian</option>
            <option value="Italian">Italian</option>
            <option value="Korean">Korean</option>
            <option value="Mexican">Mexican</option>
            <option value="Thai">Thai</option>
          </select>
          
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
