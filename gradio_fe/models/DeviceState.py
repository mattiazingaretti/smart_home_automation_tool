from typing import Any
from models.DeviceType import DeviceType

class DeviceState:

    def __init__(self, name: str, state: Any, type: DeviceType):
        self.name = name
        self.state = state
        self.type = type