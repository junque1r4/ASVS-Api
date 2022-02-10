from fastapi import APIRouter
from Config.db import connection
from Schemas.verification import verificationEntity, verificationEntitys


router = APIRouter()


@router.get("/auth")
async def auth():
    print(";")
    return verificationEntitys(connection.auth_nist.verification.find())


# TODO:
@router.post("/auth")
async def auth():
    pass


# TODO
@router.get("/session_management")
async def session_management():
    pass


# TODO
@router.get("/input_sanitization")
async def input_sanitization():
    pass
