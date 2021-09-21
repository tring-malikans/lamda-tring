import time
from typing import Dict

import jwt
from decouple import config


def token_response(token: str,id:str):
    return {
        "access_token": token,
        "user_id":id
    }

JWT_SECRET = "newadmin"


def signJWT(user_id: str,id:str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {
        'user_id': user_id,
        'expires': time.time() + 2400
    }
    return token_response(jwt.encode(payload, JWT_SECRET, algorithm="HS256").decode(),id)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token.encode(), JWT_SECRET, algorithms=["HS256"])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return None