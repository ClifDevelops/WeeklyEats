import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllMeals } from "../../store/meal";
import { removeIngredientFromGroceryList } from "../../store/grocerylist"
import "./GroceryList.css";

const GroceryList = () => {
    const dispatch = useDispatch();
    const list = useSelector((state) => state?.groceryList);
    // console.log(list)

    return (
        <div className='grocery-list-container'>
            <div className='grocery-list-title'>GROCERY LIST</div>
            {Object.values(list).map((item) => {
                return (
                  <div className='gl-individual-item-container' key={item.id}>
                    <div className='gl-individual-item-name'>{item.name}</div>
                    <div>
                      <button onClick={() => dispatch(removeIngredientFromGroceryList(item))}>Remove</button>
                    </div>
                  </div>
                );
            })}
             </div>
    )
}

export default GroceryList