import databases
import sqlalchemy

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import DatabasesCRUDRouter

DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

metadata = sqlalchemy.MetaData()
potatoes = sqlalchemy.Table(
    "potatoes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("thickness", sqlalchemy.Float),
    sqlalchemy.Column("mass", sqlalchemy.Float),
    sqlalchemy.Column("color", sqlalchemy.String),
    sqlalchemy.Column("type", sqlalchemy.String),
)
metadata.create_all(bind=engine)


class PotatoCreate(BaseModel):
    thickness: float
    mass: float
    color: str
    type: str


class Potato(PotatoCreate):
    id: int


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


router = DatabasesCRUDRouter(
    schema=Potato,
    create_schema=PotatoCreate,
    table=potatoes,
    database=database
)
app.include_router(router)