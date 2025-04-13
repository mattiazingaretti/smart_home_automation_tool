from mcp.server.fastmcp import FastMCP
import json
import asyncio
import requests

mcp = FastMCP(name="My App",  host='127.0.0.1', port=8081, log_level='DEBUG')

APP_BASE_PATH = 'http://127.0.0.1:8080'


@mcp.tool(
        description="Get the state of all devices"
)
async def devices_state() -> str:
    """function that return all the devices state."""
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.get(
                f"{APP_BASE_PATH}/devices/state/",
                headers={"Content-Type": "application/json"}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Current devices state: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching device states: {e}")
        return f"Error: {str(e)}"


#START FAN TOOLS
@mcp.tool(
        description="This tools create a new fan device and assign it a state",
)
async def create_fan(name: str, state: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.post(
                f"{APP_BASE_PATH}/fan/fans/",
                headers={"Content-Type": "application/json"},
                params={"name": name, "value": state}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching device states: {e}")
        return f"Error: {str(e)}"

@mcp.tool(
        description="This tools delete a fan device given its name and return a message ",
)
async def delete_fan(name: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.delete(
                f"{APP_BASE_PATH}/fan/fans/{name}/",
                headers={"Content-Type": "application/json"}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching device states: {e}")
        return f"Error: {str(e)}"

@mcp.tool(
        description="This tools update the state of a fan device given its name",
)
async def update_fan(name: str, state: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.put(
                f"{APP_BASE_PATH}/fan/fans/{name}/",
                headers={"Content-Type": "application/json"},
                params={"name": name, "value": state}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching device states: {e}")
        return f"Error: {str(e)}"

#START THERMOSTAT TOOLS
@mcp.tool(
        description="This tool creates a new thermostat device and assigns it a value",
)
async def create_thermostat(name: str, value: int) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.post(
                f"{APP_BASE_PATH}/thermostat/thermostats/",
                headers={"Content-Type": "application/json"},
                params={"name": name, "value": value}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error creating thermostat: {e}")
        return f"Error: {str(e)}"

@mcp.tool(
        description="This tool updates the value of a thermostat device given its name",
)
async def update_thermostat(name: str, value: int) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.put(
                f"{APP_BASE_PATH}/thermostat/thermostats/{name}/",
                headers={"Content-Type": "application/json"},
                params={"name": name, "value": value}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error updating thermostat: {e}")
        return f"Error: {str(e)}"

@mcp.tool(
        description="This tool deletes a thermostat device given its name",
)
async def delete_thermostat(name: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.delete(
                f"{APP_BASE_PATH}/thermostat/thermostats/{name}/",
                headers={"Content-Type": "application/json"}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error deleting thermostat: {e}")
        return f"Error: {str(e)}"

#START LIGHT TOOLS
@mcp.tool(
        description="This tool creates a new light device and assigns it a state",
)
async def create_light(name: str, state: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.post(
                f"{APP_BASE_PATH}/light/lights/",
                headers={"Content-Type": "application/json"},
                params={"name": name, "value": state}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error creating light: {e}")
        return f"Error: {str(e)}"

@mcp.tool(
        description="This tool updates the state of a light device given its name",
)
async def update_light(name: str, state: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.put(
                f"{APP_BASE_PATH}/light/lights/{name}/",
                headers={"Content-Type": "application/json"},
                params={"name": name, "value": state}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error updating light: {e}")
        return f"Error: {str(e)}"

@mcp.tool(
        description="This tool deletes a light device given its name",
)
async def delete_light(name: str) -> str:
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: requests.delete(
                f"{APP_BASE_PATH}/light/lights/{name}/",
                headers={"Content-Type": "application/json"}
            )
        )
        response.raise_for_status()
        
        data = response.json()
        return f"Message: {data}"

    except requests.exceptions.RequestException as e:
        print(f"Error deleting light: {e}")
        return f"Error: {str(e)}"


if __name__ == '__main__':
    mcp.run(transport='sse')
