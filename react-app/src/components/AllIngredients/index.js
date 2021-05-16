import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Redirect } from "react-router-dom";
import { getAllIngredients } from "../../store/ingredient";
import { addIngredientToGroceryList} from "../../store/grocerylist";
import "./AllIngredients.css";
import IngredientForm from "../IngredientForm";
import GroceryList from "../GroceryList";

const AllIngredients = () => {
    const dispatch = useDispatch()
    // const [loaded, setLoaded] = useState(false)
    // console.log(ingredients)
    useEffect(() => {
        dispatch(getAllIngredients());
    }, [])

    const ingredients = useSelector(state => state?.ingredient)
    const [searchTerm, setSearchTerm] = useState("");
    
    useEffect(() => { 
    }, [Object.values(ingredients).length]);
    
    // useEffect(() => {
    //     (async () => {
    //       const ingredients = await dispatch(getAllIngredients());
    //       if (ingredients) {
    //         setLoaded(true);
    //       } else {
    //         return <Redirect to="/homepage" />;
    //       }
    //     })();  
    // }, [dispatch]);
    // useEffect(() => {
    //   (async () => {
    //     const thisEvent = await dispatch(getOneEvent(Number(id)));
    //     if (thisEvent) {
    //       setLoaded(true);
    //     } else {
    //       return <Redirect to="/" />;
    //     }
    //   })();
    // }, [dispatch]);

    const addToGroceryList = (ingredient) => {
        dispatch(addIngredientToGroceryList(ingredient))
    }
    
    return (
      <div className='ingredients-page-grid'>
        
        <div className="all-ingredients-container">
          <input
            className='ingredients-search-input'
            type="text"
            placeholder="Filter your ingredient options"
            onChange={(e) => {
              setSearchTerm(e.target.value);
            }}
          />
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
                <div
                  key={ingredient.id}
                  className="ingredient-individual-container"
                >
                  <div>{ingredient.name}</div>
                  <div>{ingredient.type}</div>
                  <button
                    className="ingredient-button"
                    onClick={() => addToGroceryList(ingredient)}
                  >
                    Add to Grocery List
                  </button>
                </div>
              );
            })}
        </div>
        <div className='ingredients-page-right-side-container'>
          <IngredientForm />
          <GroceryList />
        </div>
      </div>
    );
}

export default AllIngredients