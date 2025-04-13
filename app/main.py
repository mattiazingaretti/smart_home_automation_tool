from fastapi import FastAPI
import uvicorn
from controllers.fan_controller import fan_router
from controllers.light_controller import light_router
from controllers.thermostat_controller import thermostat_router
from controllers.devices_state_controller import devices_state_router

fastApiApp = FastAPI(title="Smart Home Automation API")


@fastApiApp.get("/")
async def root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Smart Home Automation API!"}


fastApiApp.include_router(fan_router, prefix="/fan", tags=["Devices"])
fastApiApp.include_router(light_router, prefix="/light", tags=["Devices"])
fastApiApp.include_router(thermostat_router, prefix="/thermostat", tags=["Devices"])
fastApiApp.include_router(devices_state_router, prefix="/devices", tags=["Devices State"])

if __name__ == "__main__":
    uvicorn.run(fastApiApp, host="127.0.0.1", port=8080)