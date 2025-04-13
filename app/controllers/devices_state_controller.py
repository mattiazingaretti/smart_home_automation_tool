from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from config.database import get_db
from models.DeviceState import DeviceState
from models.DeviceType import DeviceType
from models.LightDevice import LightDevice
from models.FanDevice import FanDevice
from models.ThermostatDevice import ThermostatDevice
devices_state_router = APIRouter()



@devices_state_router.get("/state/")
async def get_devices_state(db: AsyncSession = Depends(get_db)):
    try:
        devices_states = []
        
        device_mappings = [
            (LightDevice, DeviceType.LIGHT),
            (FanDevice, DeviceType.FAN),
            (ThermostatDevice, DeviceType.THERMOSTAT)
        ]

        for DeviceModel, device_type in device_mappings:
            query = select(DeviceModel)
            result = await db.execute(query)
            devices = result.scalars().all()
            
            for device in devices:
                devices_states.append(
                    DeviceState(
                        name=device.name,
                        state=device.value,
                        type=device_type
                    )
                )

        devices_details = [
            {
                "name": device.name,
                "state": device.state,
                "type": device.type.value
            }
            for device in devices_states
        ]

        return devices_details
    
    except Exception as e:
        print(f"Error fetching device states: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching device states: {str(e)}"
        )