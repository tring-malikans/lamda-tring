from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.users import *

router = APIRouter()

# Get
@router.get("", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    return ResponseModel(users, "Users data retrieved successfully") \
        if len(users) > 0 \
        else ResponseModel(
        users, "Empty list returned")


# Get One
@router.get("/getone/{_id}", response_description="user data retrieved")
async def get_user_data1(_id):
    user = await retrieve_user1(_id)
    return ResponseModel(user, "user data retrieved successfully") \
        if user \
        else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")
# Get One
@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    return ResponseModel(user, "user data retrieved successfully") \
        if user \
        else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")
# Get  account select
@router.get("/accountselect/{name}", response_description="user data retrieved")
async def get_user_data(name):
    user = await retrieve_user_account(name)
    return ResponseModel(user, "user data retrieved successfully") \
        if user \
        else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")
# Get  account select
@router.get("/accountselect/balance/{id}", response_description="user data retrieved")
async def get_user_data(id):
    user = await retrieve_user_account_balance(id)
    return ResponseModel(user, "user data retrieved successfully") \
        if user \
        else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")

# Post User
@router.post("", response_description="User data added into the database")
async def add_user_data(user: UsersModel = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")


@router.put("/{id}")
async def update_user(id: str, req: UpdateUsersModel = Body(...)):
    updated_user = await update_user_data(id, req.dict())
    return ResponseModel("User with ID: {} name update is successful".format(id),
                         "User name updated successfully") \
        if updated_user \
        else ErrorResponseModel("An error occurred", 404, "There was an error updating the student.".format(id))

@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    return ResponseModel("User with ID: {} removed".format(id), "User deleted successfully") \
        if deleted_user \
        else ErrorResponseModel("An error occured", 404, "User with id {0} doesn't exist".format(id))



# sbibi
# uBDN9RU68pf16u3QRl4lcKf15qQTek34aeOL67KQQee6iPvkxpV4ymmKTBILeg9R
# pxcpxI0v2U4f3oJ2NwvZDGiIwNlBHmOhw6ACoxLBF0aPIhPX4Pxe8wsYobSdiC6y