import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './NavBar.css'

const NavBar = () => {
  return (
    <nav>
      <div className="nav-container">
        <div>
          <NavLink to="/" exact={true} activeClassName="active">
            Home
          </NavLink>
        </div>
        <div>
          <NavLink to="/homepage" exact={true} activeClassName="active">
            Homepage
          </NavLink>
        </div>
        <div>
          <NavLink to="/login" exact={true} activeClassName="active">
            Login
          </NavLink>
        </div>
        <div>
          <NavLink to="/sign-up" exact={true} activeClassName="active">
            Sign Up
          </NavLink>
        </div>
        <div>
          <NavLink to="/meals/create" exact={true} activeClassName="active">
            Add a Meal
          </NavLink>
        </div>
        <div>
          <NavLink
            to="/ingredients/create"
            exact={true}
            activeClassName="active"
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
