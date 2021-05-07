import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import IngredientForm from "./components/IngredientForm"
import MealForm from "./components/MealForm"
import NavBar from "./components/NavBar";
import Homepage from "./components/Homepage"
import Splash from "./components/Splash"
import ProtectedRoute from "./components/auth/ProtectedRoute";
// import { authenticate } from "./services/auth";
import { authenticate } from "./store/session";

function App() {
  // const [authenticated, setAuthenticated] = useState(false);
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
      <NavBar />

      <Switch>
        
        <ProtectedRoute path="/ingredients/create" exact={true}>
          <IngredientForm />
        </ProtectedRoute>
        <ProtectedRoute path="/meals/create" exact={true}>
          <MealForm />
        </ProtectedRoute>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/" exact={true}>
          <Splash />
        </Route>
        <ProtectedRoute path="/homepage" exact={true}>
          <Homepage />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
