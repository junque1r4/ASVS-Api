from Routes import routes
from fastapi import FastAPI


app = FastAPI()
app.include_router(routes.router)


@app.get("/")
async def index():
    return {"all working well here": "ok"}
