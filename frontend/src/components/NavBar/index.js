import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import Logo from '../../images/Yellow-Logo.png'
import './NavBar.css'

const NavBar = () => {
  return (
    <nav>
      <div className="nav-container">
        
        <div>
          <NavLink to="/homepage" exact={true} className="navbar-link">
            <img className="navbar-logo-home" src={Logo} />
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
          <LogoutButton />
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
