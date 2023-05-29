from fastapi import APIRouter
from Config.db import collection, get_json_file
from Schemas.verification import verificationEntitys


router = APIRouter()


@router.get("/all")
async def get_all_data() -> list[dict]:
    """
    This endpoint will return all the data from the DB.
    """
    try:
        all_data = get_json_file()
        return verificationEntitys(all_data)
    except Exception as e:
        return [{"error": str(e)}]



@router.get("/chapter/{chapter}")
async def get_chapter_data(chapter: str) -> list[dict]:
    """
        This endpoint returns a list of all the requirements for a specific chapter of the ASVS standard.
        The chapter number should be passed as a string in the URL path, for example: /chapter/1.
        Returns a list of dictionaries containing the requirements for the specified chapter.
        If the chapter is not found in the database, a message indicating that the chapter was not found is returned.
    """
    try:
        return verificationEntitys(collection.find({"chapter": f"V{chapter}"}))
    except:
        return [{"message": "Chapter not found"}]


@router.post("/load_db")
async def insert_data() -> dict:
    """
        Load the local JSON file to the database.
        This endpoint reads a JSON file from the local file system and inserts its contents into the database. 
        The JSON file must contain data in the format expected by the `verificationEntitys` schema.
        Returns:
            A dictionary with a "message" key and a string value indicating whether the data was successfully inserted into the database, or an "error" key and a 
            string value containing the error message if an exception occurred during the insertion process.
    """
    try:
        data = get_json_file()
        response = collection.insert_many(verificationEntitys(data))
        return {"message": "Successfully inserted data to the database."}
    except Exception as e:
        return {"error": str(e)}
