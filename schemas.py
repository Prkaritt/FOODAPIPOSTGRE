from email.mime import image
from pydantic import BaseModel, StrictInt, StrictStr

class FoodSchema(BaseModel):
    name : StrictStr
    price: StrictInt
    image : StrictStr

    
