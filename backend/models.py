
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TireBrand(Base):
    __tablename__ = "tire_brands"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)