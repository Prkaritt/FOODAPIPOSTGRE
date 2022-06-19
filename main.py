from fastapi import FastAPI
from foodRoutes import foodRouter
import models


app = FastAPI(title="Food Crud API",
    description="This is a API consisting of CRUD operations for Food Items.",
    version="0.0.1",
    )

app.include_router(foodRouter)

@app.get('/',tags=['Home'])
def main():
    return{
        "status" : "success",
        "message" : "API is running."
    }