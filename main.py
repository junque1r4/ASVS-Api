from Routes import routes
from fastapi import FastAPI
import json


app = FastAPI()
app.include_router(routes.router)

@app.get('/')
async def index():
    return {'ok': 'ok'}
