import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { removeIngredientFromGroceryList } from "../../store/grocerylist"
import "./GroceryList.css";

const GroceryList = () => {
    const dispatch = useDispatch();
    const list = useSelector((state) => state?.groceryList);
   

    return (
        <div className='grocery-list-container'>
            <div className='grocery-list-title'>GROCERY LIST</div>
            {Object.values(list).map((item) => {
             
              if (Array.isArray(item)) return;
                return (
                  <div className='gl-individual-item-container' key={item.id}>
                    <div className='gl-individual-item-name'>{item.name}</div>
                    <div>
                      <button className='gl-remove-button' onClick={() => dispatch(removeIngredientFromGroceryList(item))}>Remove</button>
                    </div>
                  </div>
                );
            })}
             </div>
    )
}

export default GroceryList