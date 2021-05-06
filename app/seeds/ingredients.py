from app.models import db, Ingredient

def seed_ingredients():
    return

def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
    
