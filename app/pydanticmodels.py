
#SCHEMAS--structure requests--allows auto-validation of output data adherence to format when retrurned to user
from pydantic import BaseModel, EmailStr
from datetime import date  # for default today's date insertion to date fields

#baseline schemas--for HTTP GET all
class User(BaseModel):  #for HTTP GET  extends class BaseModel
    uid: int  # unique ID number for database
    name: str
    user_name: str
    join_date: date = date.today()  # default = current date
    pw: str
    email: str
    zipcode: int
    class Config:       #makes Pydantic model compatible with ORM (SQLAlchemy)
        orm_mode = True


class Seed(BaseModel):  #for HTTP GET
    id: int
    seed_type: str
    coll_loc: str
    coll_date: date = date.today() # default = current date
    num_coll: int = 1  # default = 1 seed
    class Config:
        orm_mode = True


class Plant(BaseModel):  #for HTTP GET
    id: int
    plant_type: str
    sci_name: str
    date_acq: date = date.today()  # default = current date
    num_plants: int = 1  # default = 1 plant
    watering_week: int
    sunlight_hrs_day: int
    class Config:
        orm_mode = True


class Supply(BaseModel):  #for HTTP GET
    id: int
    supply_type: str
    brand_name: str
    purch_acq: date = date.today()  # default = current date
    num_supply: int = 1  # default = 1 item/container
    amt: int = 1  # default = 1 unit
    unit: str = "lbs."  # default = pounds; could be ounces, etc.
    class Config:
        orm_mode = True
    
# creation schemas--inherit all attributes except ID from baseline schemas--for HTTP POST
class CreateUser(User):  #inherits all attributes from class User except ID and password
    name: str
    user_name: str
    join_date: date = date.today()  # default = current date
    email: EmailStr #ensures valid email
    zipcode: int
    
class ReturnUser(User):
    uid: int
    name: str
    user_name: str
    join_date: date = date.today()  # default = current date
    email: EmailStr #ensures valid email
    zipcode: int

class CreateSeed(Seed): 
    seed_type: str
    coll_loc: str
    coll_date: date = date.today()  # default = current date
    num_coll: int = 1  # default = 1 seed

class CreatePlant(Plant):  
    plant_type: str
    sci_name: str
    date_acq: date = date.today()  # default = current date
    num_plants: int = 1  # default = 1 plant
    watering_week: int
    sunlight_hrs_day: int


class CreateSupply(Supply):  
    supply_type: str
    brand_name: str
    purch_acq: date = date.today()  # default = current date
    num_supply: int = 1  # default = 1 item/container
    amt: int = 1  # default = 1 unit
    unit: str = "lbs."  # default = pounds; could be ounces, etc.

#editing/updating schemas: inherit SOME attributes from baseline classes--FOR HTTP PUT
class EditUser(User): 
    name: str
    user_name: str
    email: str
    zipcode: int

class EditSeed(Seed):  
    seed_type: str
    coll_loc: str
    coll_date: date = date.today()  # default = current date
    num_coll: int = 1  # default = 1 seed

class EditPlant(Plant):  
    plant_type: str
    sci_name: str
    date_acq: date = date.today()  # default = current date
    num_plants: int = 1  # default = 1 plant
    watering_week: int
    sunlight_hrs_day: int

class EditSupply(Supply):  
    supply_type: str
    brand_name: str
    purch_acq: date = date.today()  # default = current date
    num_supply: int = 1  # default = 1 item/container
    amt: int = 1  # default = 1 unit
    unit: str = "lbs."  # default = pounds; could be ounces, etc.

#deletion schemas: inherit SOME attributes from baseline classes--for HTTP DELETE

class DeleteUser(User):  #inherits all attributes from class User
    pass

class DeleteSeed(Seed):  #inherits all attributes from class Seed
    pass

class DeletePlant(Plant):  #inherits all attributes from class Plant
    pass

class DeleteSupply(Supply):  #inherits all attributes from class Supply
    pass