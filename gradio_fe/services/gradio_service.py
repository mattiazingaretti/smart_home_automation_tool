
from models.DeviceState import DeviceState
import requests
from constants import Constants



def perform_action_on_device(prompt: str) -> str:
    """
    Perform an action on a device based on the provided prompt.
    
    Args:
        prompt (str): The user's prompt/query for device action
        
    Returns:
        str: Response from the MCP client
    """
    try:
        response = requests.post(
            f"{Constants.MCP_CLIENT_URL}/process",
            headers={"Content-Type": "application/json"},
            json={"query": prompt}
        )
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "No response received")

    except requests.exceptions.RequestException as e:
        print(f"Error performing action on device: {e}")
        return f"Error: {str(e)}"


def fetch_devices_state() -> list[DeviceState]:
    """
    Fetch device states by making a REST call to the backend.
    """
    try:
        response = requests.get(f"{Constants.BACKEND_URL}/devices/state")
        response.raise_for_status()  
        
        devices_data = response.json()
        
        devices = [
            DeviceState(
                name=device["name"],
                state=device["state"],
                type=device["type"]
            )
            for device in devices_data
        ]
        print(devices)        
        return devices

    except requests.exceptions.RequestException as e:
        print(f"Error fetching device states: {e}")
        return []


def format_device_state(device: DeviceState) -> str:
    return f"""
        <li style="margin-bottom: 5px;">
            <strong>Device: {device.name}:</strong> State: {device.state}
        </li>
    """

def formatted_device_states() -> str:
    
    states = fetch_devices_state()
    states_formatted = f""
    for state in states:
        formatted_state = format_device_state(state)
        states_formatted += formatted_state
    
    return f"""
        <div style="font-family: Arial, sans-serif; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
            <h3 style="color: #333;">Device States</h3>
            <ul style="list-style-type: none; padding: 0;">
                {states_formatted}
            </ul>
        </div>
        """