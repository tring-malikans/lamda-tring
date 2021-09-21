from fastapi import APIRouter, Body,Request
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.indicators import *

router = APIRouter()


# Get
@router.get("", response_description="indi retrieved")
async def get_indi():
    indi = await retrieve_indi()
    return ResponseModel(indi, "indi data retrieved successfully") \
        if len(indi) > 0 \
        else ResponseModel(
        indi, "Empty list returned")

@router.get("/taapidata/{id}", response_description="indi retrieved")
async def get_indi(id):
    indi = await retrieve_indi_tapi(id)
    return ResponseModel(indi, "indi data retrieved successfully") \
        if len(indi) > 0 \
        else ResponseModel(
        indi, "Empty list returned")

# Post User
@router.post("", response_description="indi data added into the database")
async def add_indi_data(indis: dict ):
    print(indis)
    # indi = jsonable_encoder(indis)
    new_indi = await add_indi(indis)
    return ResponseModel(new_indi, "indi added successfully.")

# # Get One
# @router.get("/getone/{_id}", response_description="user data retrieved")
# async def get_user_data1(_id):
#     user = await retrieve_user1(_id)
#     return ResponseModel(user, "user data retrieved successfully") \
#         if user \
#         else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")
# # Get One
# @router.get("/{id}", response_description="user data retrieved")
# async def get_user_data(id):
#     user = await retrieve_user(id)
#     return ResponseModel(user, "user data retrieved successfully") \
#         if user \
#         else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")
# # Get  account select
# @router.get("/accountselect/{name}", response_description="user data retrieved")
# async def get_user_data(name):
#     user = await retrieve_user_account(name)
#     return ResponseModel(user, "user data retrieved successfully") \
#         if user \
#         else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")
# # Get  account select
# @router.get("/accountselect/balance/{id}", response_description="user data retrieved")
# async def get_user_data(id):
#     user = await retrieve_user_account_balance(id)
#     return ResponseModel(user, "user data retrieved successfully") \
#         if user \
#         else ErrorResponseModel("An error occured.", 404, "User doesn'exist.")



@router.put("/update/{id}")
async def update_user(id: str, req: dict):
    updated_user = await update_indi_data(id, req)
    return ResponseModel("User with ID: {} name update is successful".format(id),
                         "success") \
        if updated_user \
        else ErrorResponseModel("An error occurred", 404, "There was an error updating the student.".format(id))

# @router.delete("/{id}", response_description="User data deleted from the database")
# async def delete_user_data(id: str):
#     deleted_user = await delete_user(id)
#     return ResponseModel("User with ID: {} removed".format(id), "User deleted successfully") \
#         if deleted_user \
#         else ErrorResponseModel("An error occured", 404, "User with id {0} doesn't exist".format(id))



# sbibi
# uBDN9RU68pf16u3QRl4lcKf15qQTek34aeOL67KQQee6iPvkxpV4ymmKTBILeg9R
# pxcpxI0v2U4f3oJ2NwvZDGiIwNlBHmOhw6ACoxLBF0aPIhPX4Pxe8wsYobSdiC6y

# sbibi
# kN58w5JBuqRF0Hi2wZddjOeyB8fyF5GFE4bI1laYlQTiWd2gqw4uL6ywDiJIODmQ
# dNcQDok7txk5HFktv2G2VMhyKJrx4phfCjsSJj4oojgxYGgeMwrohT7BzPkeKCcH