import React from "react";
import { useEffect} from "react";
import { useParams, useHistory, NavLink } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getAllMeals, deleteMealIngredient } from "../../store/meal";
import MealIngredientsForm from "../MealIngredientsForm";
import './MealDisplay.css'
import IngredientForm from "../IngredientForm";

const MealDisplay = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const { mealId } = useParams();
    const meal = useSelector(state => state?.meal[mealId])
    

    useEffect(() => {
      dispatch(getAllMeals());
    }, []);

  const deleteMI = async (mealId, ingredientId) => {
    
    await dispatch(deleteMealIngredient(mealId, ingredientId))
    await dispatch(getAllMeals());
  }
    ;
    
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
            
            <div>{meal?.meal_ingredients.map((ingredient) => {
                return (
                  <div className='meal-display-individual-ingredient'>
                    <div>{ingredient.ingredient.name}</div>
                    <div>
                      <button className='meal-individual-ingredient-remove-button' onClick={() => deleteMI(mealId, ingredient?.ingredient_id)}>remove</button>
                    </div>
                  </div>
                )})}</div>
            <MealIngredientsForm mealId={mealId} />
            <IngredientForm />
          </div>
        </div>
      </div>
    );
}

export default MealDisplay