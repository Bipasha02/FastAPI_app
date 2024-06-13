from fastapi import FastAPI
from .api.endpoints import configurations
from .database import database, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configurations.router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
