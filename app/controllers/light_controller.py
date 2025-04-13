from config.database import get_db
from models.LightDevice import LightDevice
from models.DeviceState import DeviceState
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


light_router = APIRouter()

@light_router.post("/lights/")
async def create_light_endpoint(name: str, value: str, db: AsyncSession = Depends(get_db)):
    try:
        # Check for existing light using async query
        query = select(LightDevice).where(LightDevice.name == name)
        result = await db.execute(query)
        existing_light = result.scalar_one_or_none()
        
        if existing_light:
            raise HTTPException(status_code=400, detail=f"Light with name '{name}' already exists")

        # Create new light device
        light = LightDevice(name=name, value=value)
        db.add(light)
        await db.commit()
        await db.refresh(light)

        return {"message": f"Light '{name}' created successfully", "device": light}
    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@light_router.get("/lights/{name}/")
async def read_light_endpoint(name: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(LightDevice).where(LightDevice.name == name)
        result = await db.execute(query)
        light = result.scalar_one_or_none()
        
        if not light:
            raise HTTPException(status_code=404, detail="Light not found")
        return light
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@light_router.put("/lights/{name}/")
async def update_light_endpoint(name: str, value: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(LightDevice).where(LightDevice.name == name)
        result = await db.execute(query)
        light = result.scalar_one_or_none()
        
        if not light:
            raise HTTPException(status_code=404, detail="Light not found")
            
        light.value = value
        await db.commit()
        return {"message": f"Light '{name}' updated successfully."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@light_router.delete("/lights/{name}/")
async def delete_light_endpoint(name: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(LightDevice).where(LightDevice.name == name)
        result = await db.execute(query)
        light = result.scalar_one_or_none()
        
        if not light:
            raise HTTPException(status_code=404, detail="Light not found")
            
        await db.delete(light)
        await db.commit()
        return {"message": f"Light '{name}' deleted successfully."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
