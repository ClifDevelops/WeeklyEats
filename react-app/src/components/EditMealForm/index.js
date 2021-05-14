import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useParams, useHistory } from "react-router-dom";
import { editMeal } from "../../store/meal";
import "../MealForm/MealForm.css";

const EditMealForm = () => {
  const dispatch = useDispatch();
  const [name, setName] = useState("");
  const [cuisine, setCuisine] = useState("American");
  const [recipe, setRecipe] = useState("");
  const history = useHistory()
  const { mealId } = useParams();
  const meal = useSelector((state) => state?.meal[mealId]);

  const updateName = (e) => {
    setName(e.target.value);
  };

  const updateCuisine = (e) => {
    setCuisine(e.target.value);
  };

  const updateRecipe = (e) => {
    setRecipe(e.target.value);
  };

  useEffect(() => {
      setName(meal?.name)
      setCuisine(meal?.cuisine)
      setRecipe(meal?.recipe)
  }, [])


  const onSubmit = async (e) => {
    e.preventDefault();
    const meal = {
    meal_id: mealId,
      name,
      cuisine,
      recipe,
    };
    dispatch(editMeal(meal));
    setName("");
    setCuisine("American");
    setRecipe("");
    history.push(`/meals/${mealId}`)
  };

  return (
    <div className="meal-form-container">
      <form className="meal-form" onSubmit={onSubmit}>
        <div className="meal-form-div">
          <input
            type="text"
            name="name"
            onChange={updateName}
            value={name}
            placeholder="Meal Name"
            className="meal-form-input"
          ></input>
        </div>
        <div className="meal-form-div">
          <select
            className="meal-form-select"
            name="cuisine"
            onChange={updateCuisine}
            value={cuisine}
          >
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
        <div className="meal-form-div">
          <textarea
            type="text"
            name="recipe"
            onChange={updateRecipe}
            value={recipe}
            placeholder="Recipe goes here!"
            className="meal-form-textarea"
          ></textarea>
        </div>
        <button className="meal-form-button" type="submit">
          Resubmit Meal
        </button>
      </form>
    </div>
  );
};

export default EditMealForm;
