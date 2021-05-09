import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { addToMeals } from "../../store/meal";
import { getAllIngredients } from "../../store/ingredient";
import "./MealIngredientsForm.css";

const MealIngredientsForm = () => {
    const dispatch = useDispatch();

    const ingredients = useSelector((state) => state?.ingredient?.ingredients);
    console.log(ingredients)

    const [ingredient_id, setIngredient_id] = useState("");
    const [ingredient_quantity, setIngredient_quantity] = useState("");
    const [measurement_unit, setMeasurement_unit] = useState("");

    useEffect(() => {
      dispatch(getAllIngredients());
    }, []);

    const updateMeasurementUnit = (e) => {
       setMeasurement_unit(e.target.value);
    };
     const onSubmit = async (e) => {
       e.preventDefault();
    //    const meal = {
    //      name,
    //      cuisine,
    //      recipe,
    //    };
    //    dispatch(addToMeals(meal));
    //    setName("");
    //    setCuisine("");
    //    setRecipe("");
     };

    return (
      <form onSubmit={onSubmit}>
        <div>
          <div>
            <label htmlFor="ingredient_quantity">Ingredient Quantity</label>
          </div>
          <div>
            <input
              onChange={(e) => setIngredient_quantity(e.target.value)}
              name="ingredient_quantity"
              type="number"
              step="0.5"
              className="ingredient-quantity-input"
            ></input>
          </div>
          <div>
            <label htmlFor="measurement_unit">Measurement Unit</label>
          </div>
          <div>
            <select
              name="measurement_unit"
              onChange={updateMeasurementUnit}
              value={measurement_unit}
            >
              <option value="tsp">tsp</option>
              <option value="tbsp">tbsp</option>
              <option value="fl oz">fl oz</option>
              <option value="c">c</option>
              <option value="pt">pt</option>
              <option value="qt">qt</option>
              <option value="mL">mL</option>
              <option value="L">L</option>
              <option value="lb">lb</option>
              <option value="oz">oz</option>
              <option value="g">g</option>
              <option value="mg">mg</option>
              <option value="kg">kg</option>
              <option value="each">each</option>
            </select>
          </div>
        </div>
      </form>
    );
}

export default MealIngredientsForm;