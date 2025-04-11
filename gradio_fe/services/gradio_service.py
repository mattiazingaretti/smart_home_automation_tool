
from models.DeviceState import DeviceState
import requests
from constants import Constants




def fetch_devices_state() -> list[DeviceState]:
    """
    Fetch device states by making a REST call to the backend.
    """
    try:
        response = requests.get(f"{Constants.BACKEND_URL}/devices/states")
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

def gradio_process_prompt(prompt: str) -> str:
    
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