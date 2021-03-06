from sqlalchemy import Column, Integer, String
from app.database.base_class import Base

class Place(Base):
    __tablename__ = "places"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    image = Column(String)