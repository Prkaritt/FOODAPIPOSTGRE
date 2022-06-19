from config import Base
from sqlalchemy import Column, Integer, String, true
from config import engine


class Food(Base):
    __tablename__ = "foodTable"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)
    price = Column(Integer)

Base.metadata.create_all(bind=engine)


