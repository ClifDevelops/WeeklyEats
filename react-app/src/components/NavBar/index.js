import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './NavBar.css'

const NavBar = () => {
  return (
    <nav>
      <div className="nav-container">
        <div>
          <NavLink to="/" exact={true} className="navbar-link">
            Home
          </NavLink>
        </div>
        <div>
          <NavLink to="/homepage" exact={true} className="navbar-link">
            Homepage
          </NavLink>
        </div>
        <div>
          <NavLink to="/meals" exact={true} className="navbar-link">
            Meals
          </NavLink>
        </div>
        <div>
          <NavLink to="/meals/create" exact={true} className="navbar-link">
            Add a Meal
          </NavLink>
        </div>
        <div>
          <NavLink to="/ingredients" exact={true} className="navbar-link">
            Ingredients
          </NavLink>
        </div>
        <div>
          <NavLink
            to="/ingredients/create"
            exact={true}
            className="navbar-link"
          >
            Add an Ingredient
          </NavLink>
        </div>

        <div>
          <LogoutButton />
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
