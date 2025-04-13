from fastapi import APIRouter, HTTPException
from models.ThermostatDevice import ThermostatDevice
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from config.database import get_db

thermostat_router = APIRouter()

@thermostat_router.post("/thermostats/")
async def create_thermostat_endpoint(name: str, value: int, db: AsyncSession = Depends(get_db)):
    try:
        query = select(ThermostatDevice).where(ThermostatDevice.name == name)
        result = await db.execute(query)
        existing_thermostat = result.scalar_one_or_none()
        
        if existing_thermostat:
            raise HTTPException(status_code=400, detail=f"Thermostat with name '{name}' already exists")

        thermostat = ThermostatDevice(name=name, value=value)
        db.add(thermostat)
        await db.commit()
        await db.refresh(thermostat)

        return {"message": f"Thermostat '{name}' created successfully", "device": thermostat}
    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@thermostat_router.get("/thermostats/{name}/")
async def read_thermostat_endpoint(name: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(ThermostatDevice).where(ThermostatDevice.name == name)
        result = await db.execute(query)
        thermostat = result.scalar_one_or_none()
        
        if not thermostat:
            raise HTTPException(status_code=404, detail="Thermostat not found")
        return thermostat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@thermostat_router.put("/thermostats/{name}/")
async def update_thermostat_endpoint(name: str, value: int, db: AsyncSession = Depends(get_db)):
    try:
        query = select(ThermostatDevice).where(ThermostatDevice.name == name)
        result = await db.execute(query)
        thermostat = result.scalar_one_or_none()
        
        if not thermostat:
            raise HTTPException(status_code=404, detail="Thermostat not found")
            
        thermostat.value = value
        await db.commit()
        return {"message": f"Thermostat '{name}' updated successfully"}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@thermostat_router.delete("/thermostats/{name}/")
async def delete_thermostat_endpoint(name: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(ThermostatDevice).where(ThermostatDevice.name == name)
        result = await db.execute(query)
        thermostat = result.scalar_one_or_none()
        
        if not thermostat:
            raise HTTPException(status_code=404, detail="Thermostat not found")
            
        await db.delete(thermostat)
        await db.commit()
        return {"message": f"Thermostat '{name}' deleted successfully"}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))