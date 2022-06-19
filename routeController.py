from this import d
from sqlalchemy.orm import Session

from schemas import FoodSchema
from models import Food

from config import SessionLocal

def get_all_food():
    db = SessionLocal()
    _food = db.query(Food).all()
    return _food

def get_food(id):
    db = SessionLocal()
    _food = db.query(Food).filter( Food.id == id ).first()
    return _food

def createFood(food:FoodSchema):
    db = SessionLocal()
    _food = Food(name=food.name,image=food.image,price=food.price)
    db.add(_food)
    db.commit()
    db.refresh(_food)
    return _food

def deleteFood(id):
    db = SessionLocal()
    db.query(Food).filter( Food.id == id ).delete()
    return

def updateFood(id,food:FoodSchema):
    db = SessionLocal()
    _food = db.query(Food).filter( Food.id == id ).first()
    _food.name = food.name
    _food.image = food.image
    _food.price = food.price
    db.commit()
    db.refresh(_food)
    return _food
    
