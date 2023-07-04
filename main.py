from fastapi import FastAPI

from routes import inventory


app = FastAPI()

app.include_router(inventory.router)


@app.get("/healthcheck", tags=["healthcheck"])
async def healthcheck():
    return {"healthcheck": "oksasdasaa"}
