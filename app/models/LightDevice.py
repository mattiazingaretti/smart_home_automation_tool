from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LightDevice(Base):
    __tablename__ = "light_device"

    name = Column(String, primary_key=True)
    value = Column(String)

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"LightDevice(name={self.name}, value={self.value})"
    