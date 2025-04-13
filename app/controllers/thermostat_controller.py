from fastapi import APIRouter, HTTPException
from services.devices_repository import (
    create_thermostat,
    read_thermostat,
    update_thermostat,
    delete_thermostat,
)
from models.DeviceState import DeviceState

thermostat_router = APIRouter()



@thermostat_router.post("/thermostats/")
async def create_thermostat_endpoint(name: str, value: int):
    try:
        create_thermostat(name, value)
        return {"message": f"Thermostat '{name}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@thermostat_router.get("/thermostats/{name}")
async def read_thermostat_endpoint(name: str):
    try:
        thermostat = read_thermostat(name)
        if not thermostat:
            raise HTTPException(status_code=404, detail="Thermostat not found")
        return thermostat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@thermostat_router.put("/thermostats/{name}")
async def update_thermostat_endpoint(name: str, value: int):
    try:
        update_thermostat(name, value)
        return {"message": f"Thermostat '{name}' updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@thermostat_router.delete("/thermostats/{name}")
async def delete_thermostat_endpoint(name: str):
    try:
        delete_thermostat(name)
        return {"message": f"Thermostat '{name}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))