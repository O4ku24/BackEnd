from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase


engine = create_engine(
    "sqlite:///db.sqlite",
    echo=True
)



class Model(DeclarativeBase):
    pass