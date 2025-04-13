from models.FanDevice import FanDevice
from config.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

fan_router = APIRouter()

@fan_router.post("/fans/")
async def create_fan_endpoint(name: str, value: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(FanDevice).where(FanDevice.name == name)
        result = await db.execute(query)
        existing_fan = result.scalar_one_or_none()
        
        if existing_fan:
            raise HTTPException(status_code=400, detail=f"Fan with name '{name}' already exists")

        fan = FanDevice(name=name, value=value)
        db.add(fan)
        await db.commit()
        await db.refresh(fan)

        return {"message": f"Fan '{name}' created successfully", "device": fan}
    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@fan_router.get("/fans/{name}/")
async def read_fan_endpoint(name: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(FanDevice).where(FanDevice.name == name)
        result = await db.execute(query)
        fan = result.scalar_one_or_none()
        
        if not fan:
            raise HTTPException(status_code=404, detail="Fan not found")
        return fan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@fan_router.put("/fans/{name}/")
async def update_fan_endpoint(name: str, value: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(FanDevice).where(FanDevice.name == name)
        result = await db.execute(query)
        fan = result.scalar_one_or_none()
        
        if not fan:
            raise HTTPException(status_code=404, detail="Fan not found")
            
        fan.value = value
        await db.commit()
        return {"message": f"Fan '{name}' updated successfully."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@fan_router.delete("/fans/{name}/")
async def delete_fan_endpoint(name: str, db: AsyncSession = Depends(get_db)):
    try:
        query = select(FanDevice).where(FanDevice.name == name)
        result = await db.execute(query)
        fan = result.scalar_one_or_none()
        
        if not fan:
            raise HTTPException(status_code=404, detail="Fan not found")
            
        await db.delete(fan)
        await db.commit()
        return {"message": f"Fan '{name}' deleted successfully."}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
