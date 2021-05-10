from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(40), nullable = False, unique = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  hashed_password = db.Column(db.String(255), nullable = False)

  user_meals = db.relationship("UserMeal", back_populates="user")


  @property
  def password(self):
    return self.hashed_password


  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)


  def to_dict(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email
    }


class Meal(db.Model):
  __tablename__ = 'meals'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)
  cuisine = db.Column(db.String(50), nullable=False)
  recipe = db.Column(db.Text(), nullable=True)

  meal_ingredients = db.relationship("MealIngredient", back_populates="meal")
  user_meals = db.relationship("UserMeal", back_populates="meal")


  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "cuisine": self.cuisine,
      "recipe": self.recipe
    }




class Ingredient(db.Model):
  __tablename__ = 'ingredients'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False, unique=True)
  type = db.Column(db.String(50), nullable=False)

  meal_ingredients = db.relationship("MealIngredient", back_populates="ingredient")
  
  def to_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "type": self.type,
    }


class MealIngredient(db.Model):
    __tablename__ = "meal_ingredients"
    __table_args__ = (
        db.UniqueConstraint('meal_id', 'ingredient_id', name='ingredient_once_per_meal'),
    )

    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)
    ingredient_quantity = db.Column(db.Float, nullable=False)
    measurement_unit = db.Column(db.String(50), nullable=False)

    ingredient = db.relationship(
        "Ingredient", back_populates="meal_ingredients")
    meal = db.relationship("Meal", back_populates="meal_ingredients")
    

    def to_dict(self):
        return {
            "id": self.id,
            "meal_id": self.meal_id,
            "ingredient_id": self.ingredient_id,
            "ingredient_quantity": self.ingredient_quantity,
            "measurement_unit": self.measurement_unit
        }

class UserMeal(db.Model):
  __tablename__='user_meals'
  __table_args__ = (
    db.UniqueConstraint('user_id', 'meal_id', name='unique_user_meal'),
  )

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)

  user = db.relationship("User", back_populates='user_meals')
  meal = db.relationship("Meal", back_populates='user_meals')

  def to_dict(self):
      return {
          "id": self.id,
          "user_id": self.user_id,
          "meal_id": self.meal_id
      }


