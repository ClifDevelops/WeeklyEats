from flask.cli import AppGroup
from .users import seed_users, undo_users
from .ingredients import seed_ingredients, undo_ingredients, seed_meal_ingredients, undo_meal_ingredients
from .meals import seed_meals, seed_user_meals, undo_meals, undo_user_meals

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_ingredients()
    seed_meals()
    seed_user_meals()
    seed_meal_ingredients()

    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_ingredients()
    undo_meals()
    undo_user_meals()
    undo_meal_ingredients()
    # Add other undo functions here
