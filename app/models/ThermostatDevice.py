from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ThermostatDevice(Base):
    __tablename__ = "thermostat_device"

    name = Column(String, primary_key=True)
    value = Column(Integer)

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"ThermostatDevice(name={self.name}, value={self.value})"