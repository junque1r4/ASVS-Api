from fastapi import APIRouter
from Config.db import collection, get_json_file
from Schemas.verification import verificationEntity, verificationEntitys
from Models.models import Requirement


router = APIRouter()


@router.get("/import")
async def index():
    return get_json_file()


@router.get('/all')
async def auth():
    return verificationEntitys(collection.find())


@router.post('/all')
async def insert_requirement(requirement: Requirement):
    collection.insert_one(requirement.dict())
    return verificationEntity(collection.find_one(requirement.dict()))


# TODO: implemnt /auth
@router.get('/auth')
async def auth():
    pass


# TODO: implemnt /session_management
@router.get('/session_management')
async def session_management():
    pass


# TODO: implemnt /input_sanitization
@router.get('/input_sanitization')
async def input_sanitization():
    pass
