from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(40), nullable = False, unique = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  hashed_password = db.Column(db.String(255), nullable = False)

  meals = db.relationship(
    "Meal",
    secondary=user_meals,
    back_populates="users"
  )

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
  name = db.Column(db.String(100), nullable=False)
  cuisine = db.Column(db.String(50), nullable=False)
  recipe = db.Column(db.Text(), nullable=False)

  mealIngredients = db.relationship("MealIngredient", back_populates="meal")

  users = db.relationship(
    "User",
    secondary=user_meals,
    back_populates="meals"
  )

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "cuisine": self.cuisine,
      "recipe": self.recipe
    }

user_meals = db.Table(
    "user_meals",
    db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("users.id"),
        primary_key=True
    ),
    db.Column(
        "meal_id",
        db.Integer,
        db.ForeignKey("meals.id"),
        primary_key=True
    )
)


class Ingredient(db.Model):
  __tablename__ = 'ingredients'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  type = db.Column(db.String(50), nullable=False)
  measurementUnit = db.Column(db.String(50), nullable=False)

  mealIngredients = db.relationship("MealIngredient", back_populates="ingredient")
  def to_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "type": self.type,
        "measurementUnit": self.measurementUnit
    }


class MealIngredient(db.Model):
    __tablename__ = "mealIngredients"
    __table_args__ = (
        db.UniqueConstraint('mealId', 'ingredientId', name='ingredient_once_per_meal'),
    )

    id = db.Column(db.Integer, primary_key=True)
    mealId = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)
    ingredientId = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)
    ingredientQuantity = db.Column(db.Float, nullable=False)

    ingredient = db.relationship(
        "Ingredient", back_populates="mealIngredients")
    meal = db.relationship("Meal", back_populates="mealIngredients")
    

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "coinId": self.coinId,
            "quantity": self.quantity,
            "averagePrice": self.averagePrice
        }

# class UserMeal(db.Model):
#   __tablename__='userMeals'
#   __table_args__ = (
#     db.UniqueConstraint('userId', 'mealId', name='unique_userMeal')
#   )

#   id = db.Column(db.Integer, primary_key=True)
#   userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#   mealId = db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)



