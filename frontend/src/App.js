import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import IngredientForm from "./components/IngredientForm"
import AllIngredients from "./components/AllIngredients"
import MealForm from "./components/MealForm"
import MealDisplay from "./components/MealDisplay"
import Meals from "./components/Meals"
import NavBar from "./components/NavBar";
import Footer from "./components/Footer"
import Homepage from "./components/Homepage"
import Splash from "./components/Splash"
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import ProtectedRoute from "./components/auth/ProtectedRoute";

import { authenticate } from "./store/session";
import EditMealForm from "./components/EditMealForm";

function App() {
  
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>

      <Switch>
        <Route path="/" exact={true}>
          <Splash />
          <Footer />
        </Route>
        <Route path="/login" exact={true}>
          <LoginForm />
          <Footer />
        </Route>
        <Route path="/signup" exact={true}>
          <SignUpForm/>
          <Footer />
        </Route>
        <ProtectedRoute path="/ingredients/create" exact={true}>
          <NavBar />
          <IngredientForm />
          <Footer />
        </ProtectedRoute>
        <ProtectedRoute path="/ingredients" exact={true}>
          <NavBar />
          <AllIngredients />
          <Footer />
        </ProtectedRoute>
        <ProtectedRoute path="/meals/create" exact={true}>
          <NavBar />
          <MealForm />
          <Footer />
        </ProtectedRoute>
        <ProtectedRoute path="/meals" exact={true}>
          <NavBar />
          <Meals />
          <Footer />
        </ProtectedRoute>
        <ProtectedRoute path="/meals/:mealId" exact={true}>
          <NavBar />
          <MealDisplay />
          <Footer />
        </ProtectedRoute>
        <ProtectedRoute path="/meals/:mealId/edit" exact={true}>
          <NavBar />
          <EditMealForm />
          <Footer />
        </ProtectedRoute>
        <ProtectedRoute path="/homepage" exact={true}>
          <NavBar />
          <Homepage />
          <Footer />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
