from sqlalchemy import Column, String, Enum as SQLAEnum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

Base = declarative_base()



class FanDevice(Base):
    __tablename__ = "fan_device"

    name = Column(String, primary_key=True)
    value = Column(String)

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"FanDevice(name={self.name}, value={self.value})"