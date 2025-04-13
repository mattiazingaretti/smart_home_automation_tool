from models.DeviceState import DeviceState
from services.devices_repository import create_light, delete_light, read_light, update_light
from fastapi import APIRouter, HTTPException

light_router = APIRouter()


@light_router.post("/lights/")
async def create_light_endpoint(name: str, value: str):
    try:
        create_light(name, value)
        return {"message": f"Light '{name}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@light_router.get("/lights/{name}")
async def read_light_endpoint(name: str):
    try:
        light = read_light(name)
        if not light:
            raise HTTPException(status_code=404, detail="Light not found")
        return light
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@light_router.put("/lights/{name}")
async def update_light_endpoint(name: str, value: str):
    try:
        update_light(name, value)
        return {"message": f"Light '{name}' updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@light_router.delete("/lights/{name}")
async def delete_light_endpoint(name: str):
    try:
        delete_light(name)
        return {"message": f"Light '{name}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
