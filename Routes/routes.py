from fastapi import APIRouter
from Config.db import collection, get_json_file
from Schemas.verification import verificationEntitys


router = APIRouter()


@router.get("/all")
async def auth():
    """
    This endpoint will return all the data from the DB.
    """
    try:
        all_data = get_json_file()
        return verificationEntitys(all_data)
    except Exception as e:
        return {"error": str(e)}


@router.get("/chapter/{chapter}")
async def auth(chapter: str):
    """
    This endpoint will return all the requirements for a specific chapter
    Ex: /chapter/1
    """
    try:
        return verificationEntitys(collection.find({"chapter": f"V{chapter}"}))
    except:
        return {"message": "Chapter not found"}
    return


@router.post("/load_db")
async def insert_data():
    """
    This endpoint is load the local json file to the database.
    """
    try:
        data = get_json_file()
        response = collection.insert_many(verificationEntitys(data))
        return {"message": "Successfully inserted data to the database."}
    except Exception as e:
        return {"error": str(e)}
