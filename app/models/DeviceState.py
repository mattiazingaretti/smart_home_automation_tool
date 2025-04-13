from typing import Any
from dataclasses import dataclass
from models.DeviceType import DeviceType


@dataclass
class DeviceState:

    def __init__(self, name: str, state: Any, type: DeviceType):
        self.name = name
        self.state = state
        self.type = type