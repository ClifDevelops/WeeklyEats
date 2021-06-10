import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addToMealIngredients, getAllMeals } from "../../store/meal";
import { getAllIngredients } from "../../store/ingredient";
import "./MealIngredientsForm.css";

const MealIngredientsForm = ({mealId}) => {
    const dispatch = useDispatch();
    

    const ingredients = useSelector((state) => state?.ingredient);
    

    const [ingredient_id, setIngredient_id] = useState("");
    const [searchTerm, setSearchTerm] = useState("")
    

    useEffect(() => {
      dispatch(getAllIngredients());
    }, []);

     const onSubmit = async (e) => {
       e.preventDefault();
       const mealIngredient = {
         meal_id: mealId,
         ingredient_id,
        
       };
       await dispatch(addToMealIngredients(mealIngredient));
       await dispatch(getAllMeals());
       setIngredient_id("");
      
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
                <option isdisabled='true' value={null}>Select an ingredient</option>
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
                      <option key={ingredient?.id} value={ingredient?.id}>{ingredient?.name}</option>
                    );
                  })}
              </select>
            </div>
            
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