import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom"
import { addToMealIngredients, getAllMeals } from "../../store/meal";
import { getAllIngredients } from "../../store/ingredient";
import "./MealIngredientsForm.css";

const MealIngredientsForm = ({mealId}) => {
    const dispatch = useDispatch();
    const history = useHistory();

    const ingredients = useSelector((state) => state?.ingredient);
    

    const [ingredient_id, setIngredient_id] = useState("");
    const [searchTerm, setSearchTerm] = useState("")
    // const [ingredient_quantity, setIngredient_quantity] = useState(1);
    // const [measurement_unit, setMeasurement_unit] = useState("each");

    useEffect(() => {
      dispatch(getAllIngredients());
    }, []);

    // useEffect(() => {
    //     console.log('-----------');
    //     console.log('searchTerm :: ', searchTerm);
    //     console.log('ingredient_id OLD:: ', ingredient_id)
    
    //     // every time search term changes (so in a useEffect that rerenders off of searchTerm)
    //     // the value of the selectbox should be the first item in the collection
    //     // of filtered results
    //     // eg setIngredient_id(filteredResults[0])

    // }, [searchTerm])

    const printMe = (e) => {
      console.log(e)
    }

    // const updateMeasurementUnit = (e) => {
    //    setMeasurement_unit(e.target.value);
    // };
     const onSubmit = async (e) => {
       e.preventDefault();
       const mealIngredient = {
         meal_id: mealId,
         ingredient_id,
        //  ingredient_quantity,
        //  measurement_unit,
       };
       await dispatch(addToMealIngredients(mealIngredient));
       await dispatch(getAllMeals());
       setIngredient_id(1);
      //  history.push(`/meals/${mealId}`)
      //  setIngredient_quantity(1);
      //  setMeasurement_unit("each");
     };
    if (ingredients) {
    return (
      <div className="meal-ingredient-form-container">
        <form onSubmit={onSubmit}>
          <div>
            <div></div>
            <div>
              <input
                type="text"
                className="meal-ingredient-form-input"
                placeholder="Filter your options, select from dropdown"
                onChange={(e) => {
                  setSearchTerm(e.target.value);
                }}
              />
            </div>
            <div>
              <select
                name="ingredient_id"
                value={ingredient_id}
                onChange={(e) => setIngredient_id(e.target.value)}
                required
                className="meal-ingredient-form-input"
              >
                {Object.values(ingredients)
                  .filter((ingredient) => {
                    if (searchTerm === "") {
                      return ingredient;
                    } else if (
                      ingredient?.name
                        .toLowerCase()
                        .includes(searchTerm.toLowerCase()) ||
                      ingredient?.type
                        .toLowerCase()
                        .includes(searchTerm.toLowerCase())
                    ) {
                      return ingredient;
                    }
                  })
                  .map((ingredient) => {
                    return (
                      <option value={ingredient?.id}>{ingredient?.name}</option>
                    );
                  })}
              </select>
            </div>
            {/* <div>
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
            </div> */}
          </div>
          <button className="meal-ingredient-form-button" type="submit">
            Add to Meal
          </button>
        </form>
      </div>
    );
  } else {
    return (
      <div></div>
    )
  }
}

export default MealIngredientsForm;