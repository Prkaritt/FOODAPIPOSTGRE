from fastapi import APIRouter,Depends,Response
from schemas import FoodSchema
from models import Food
import routeController

from config import SessionLocal

foodRouter = APIRouter(prefix='/food',tags=['Food'])




@foodRouter.get('/')
def allFoods(response:Response):
    _data = routeController.get_all_food()
    response.status_code = 200
    return  {
        "status" : "success",
        "message" : "All Food Items.",
        "result" : _data
    }

@foodRouter.get('/{id}')
def get_food(id):
    _data = routeController.get_food(id)
    message = "No item with that id found" if _data == None else "Food Item Found." 

    return{
        "status" : "success",
        "message" : message,
        "result" : _data,
    
    }

@foodRouter.delete('/{id}')
def delete_food(id):
    routeController.deleteFood(id)
    return 

@foodRouter.post('/')
def createFood(response:Response,food:FoodSchema):
    _data = routeController.createFood(food)
    response.status_code = 200
    return{
        "status" : "success",
        "message" : "A new item has been added.",
        "result" : _data
    }
@foodRouter.put('/{id}')
def update_food(response:Response,id,food:FoodSchema):
    _food = routeController.updateFood(id,food)
    response.status_code = 200
    return{
        "status" : "success",
        "message" : "Food Item Updated",
        "result":_food
    }
