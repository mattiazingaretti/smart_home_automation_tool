from models.DeviceState import DeviceState
from fastapi import APIRouter, HTTPException
from services.devices_repository import fetch_devices_state

devices_state_router = APIRouter()


@devices_state_router.get("/state")
async def read_light_endpoint():
    try:
        devices = fetch_devices_state()
        devices_details = [
            {
                "name": device.name,
                "state": device.state,
                "type": device.type.value
            }
            for device in devices
        ]
        print(devices_details)
        return devices_details
    except Exception as e:
        print({"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))
