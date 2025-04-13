from models.DeviceState import DeviceState
from services.devices_repository import create_fan, delete_fan, read_fan, update_fan
from fastapi import APIRouter, HTTPException

fan_router = APIRouter()


@fan_router.post("/fans/")
async def create_fan_endpoint(name: str, value: str):
    try:
        create_fan(name, value)
        return {"message": f"Fan '{name}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@fan_router.get("/fans/{name}")
async def read_fan_endpoint(name: str):
    try:
        fan = read_fan(name)
        if not fan:
            raise HTTPException(status_code=404, detail="Fan not found")
        return fan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@fan_router.put("/fans/{name}")
async def update_fan_endpoint(name: str, value: str):
    try:
        update_fan(name, value)
        return {"message": f"Fan '{name}' updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@fan_router.delete("/fans/{name}")
async def delete_fan_endpoint(name: str):
    try:
        delete_fan(name)
        return {"message": f"Fan '{name}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
