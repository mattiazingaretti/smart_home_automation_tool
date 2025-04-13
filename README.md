# Smart Home Automation Tool

A distributed system for managing and controlling smart home devices through natural language processing using Google's Gemini AI.

## Author
- Mattia Zingaretti - SW Engineer @ [Blue Reply](https://www.reply.com/blue-reply/it) - [LinkedIn](https://www.linkedin.com/in/zingaretti-mattia/)

Feel free to contact me for any questions or collaboration opportunities.


## Demo
1. Once we have everything Up and Running navigate to the Gradio base URL and check the state of the devices from this tab:
![alt text](image-1.png)
2. Then prompt our MCP Client with a natural language command like "Set the light KitchenLight to OFF" and hit generate
![alt text](image-2.png)
3. Then check the state of the devices again to see the changes:
![alt text](image-3.png)
## System Architecture

The project consists of four main components:

1. **Backend API** (Port 8080)
   - Handles CRUD operations for devices
   - Manages device states in PostgreSQL database
   - Provides REST endpoints for device control

2. **MCP Server** (Port 8081)
   - Manages tool definitions
   - Handles Server-Sent Events (SSE)
   - Provides interface for device state queries

3. **MCP Client** (Port 8082)
   - Integrates with Google Gemini AI
   - Processes natural language commands
   - Translates commands to device actions

4. **Gradio Frontend** (Port 7860)
   - Provides web interface for device control
   - Displays device states
   - Accepts natural language input

## Prerequisites

- Python 3.10 or higher
- PostgreSQL database
- Google Gemini API key

<hr>
## App Directory Structure

### Services Overview

The `app` directory contains the core backend services:

```
app/
├── controllers/           # API endpoint controllers
│   ├── devices_state_controller.py    # Handles device state queries
│   ├── fan_controller.py             # Fan device CRUD operations
│   ├── light_controller.py           # Light device CRUD operations
│   └── thermostat_controller.py      # Thermostat device CRUD operations
├── models/               # Database models and types
│   ├── DeviceState.py              # Device state representation
│   ├── DeviceType.py              # Device type enumerations
│   ├── FanDevice.py              # Fan device model
│   ├── LightDevice.py            # Light device model
│   └── ThermostatDevice.py       # Thermostat device model
├── config/               # Configuration files
│   └── database.py               # Database connection setup
└── static/              # SQL scripts
    ├── ddl.sql                   # Database schema
    └── dml.sql                   # Sample data
```

### Backend Components

1. **Controllers**
   - `devices_state_controller.py`: Aggregates states from all devices
   - `fan_controller.py`: Manages fan devices (ON/OFF/LOW/MEDIUM/HIGH)
   - `light_controller.py`: Manages light devices (ON/OFF)
   - `thermostat_controller.py`: Manages thermostat devices (18-30°C)

2. **Models**
   - SQLAlchemy ORM models for database interactions
   - Device state representations
   - Device type enumerations
   - Table constraints and validations

3. **Configuration**
   - Database connection management
   - Environment variable handling
   - Async session management

### Installation Guide

1. Set up the virtual environment:
```bash
cd app
python -m venv .venv
```

2. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- fastapi: Web framework
- uvicorn: ASGI server
- psycopg2: PostgreSQL adapter
- python-dotenv: Environment management
- sqlalchemy: ORM
- asyncpg: Async PostgreSQL

4. Set up the database:
```bash
# Create tables
psql -U postgres -d postgres -f static/ddl.sql

# Load sample data (optional)
psql -U postgres -d postgres -f static/dml.sql
```

5. Configure environment variables:
```bash
# .env file
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
```

6. Run the application:
```bash
python main.py
```

The server will start at `http://127.0.0.1:8080`

### API Documentation

#### Device State Endpoints
- `GET /devices/state/`: Get all device states

#### Fan Endpoints
- `POST /fan/fans/`: Create fan device
- `GET /fan/fans/{name}/`: Get fan state
- `PUT /fan/fans/{name}/`: Update fan state
- `DELETE /fan/fans/{name}/`: Delete fan device

#### Light Endpoints
- `POST /light/lights/`: Create light device
- `GET /light/lights/{name}/`: Get light state
- `PUT /light/lights/{name}/`: Update light state
- `DELETE /light/lights/{name}/`: Delete light device

#### Thermostat Endpoints
- `POST /thermostat/thermostats/`: Create thermostat
- `GET /thermostat/thermostats/{name}/`: Get thermostat state
- `PUT /thermostat/thermostats/{name}/`: Update thermostat
- `DELETE /thermostat/thermostats/{name}/`: Delete thermostat`

<hr>
## Gradio Frontend Directory Structure

### Services Overview

The `gradio_fe` directory contains the frontend interface components:

```
gradio_fe/
├── interfaces/              # Gradio interface components
│   ├── action_interface.py  # Device control interface
│   └── devices_interface.py # Device state display interface
├── models/                  # Data models
│   ├── DeviceState.py      # Device state representation
│   └── DeviceType.py       # Device type enums
├── services/               # Backend services
│   └── gradio_service.py   # API integration services
├── constants.py           # Configuration constants
├── main.py               # Main application entry
└── requirements.txt      # Dependencies
```

### Frontend Components

1. **Interfaces**
   - `action_interface.py`: Provides natural language input for device control
   - `devices_interface.py`: Displays current state of all devices

2. **Services**
   - `gradio_service.py`: 
     - Handles communication with MCP Client
     - Manages device state fetching
     - Processes natural language commands
     - Formats device state display

3. **Models**
   - Device state and type definitions
   - Data structure implementations
   - Type safety enforcement

### Installation Guide

1. Set up the virtual environment:
```bash
cd gradio_fe
python -m venv .venv
```

2. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- gradio: Web interface framework
- fastapi: API framework
- uvicorn: ASGI server

4. Configure constants (if needed):
```python
# constants.py
class Constants:
    BACKEND_URL = "http://127.0.0.1:8080"
    MCP_CLIENT_URL = "http://127.0.0.1:8082"
```

5. Run the application:
```bash
python main.py
```

The Gradio interface will be available at `http://127.0.0.1:7860`

### Features

1. **Device State Tab**
   - Displays all connected devices
   - Shows current state of each device
   - Auto-refreshes on state changes
   - Formatted HTML display

2. **Action Tab**
   - Natural language input field
   - Processes commands like:
     - "Turn on the living room light"
     - "Set bedroom fan to medium"
     - "Set kitchen thermostat to 24"
   - Real-time feedback on actions

### API Integration

The frontend integrates with two backend services:
1. Backend API (`:8080`) for device state queries
2. MCP Client (`:8082`) for natural language processing

### Error Handling

- Connection error management
- Invalid command feedback
- State update validation
- User-friendly error messages

<hr>
## MCP Client Directory Structure

### Services Overview

The `mcp-client` directory contains the natural language processing integration:

```
mcp-client/
├── __init__.py          # Package initialization
├── main.py             # FastAPI application
├── pyproject.toml      # Project dependencies
├── requirements.txt    # Standard dependencies
└── uv.lock            # UV dependency lock file
```

### Core Components

1. **FastAPI Application** (`main.py`)
   - Handles natural language processing requests
   - Integrates with Google Gemini AI
   - Manages MCP Server communication
   - Processes tool invocations

2. **Dependencies**
   - Google Gemini AI integration
   - FastAPI web framework
   - MCP client libraries
   - Environment configuration

### Features
- Natural language command processing
- Integration with Google's Gemini AI
- Real-time tool execution
- Async request handling
- Error management and reporting

### Installation with UV

1. Install [UV package manager](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)

2. Move to the right directory and initialize a virtual environment:
```bash
cd mcp-client
uv venv
```

3. Install dependencies using UV:
```bash
    uv sync
```
4. Activate virtual environment:
```bash
# Windows
.venv\Scripts\activate.bat
# Linux/macOS   
source .venv/bin/activate
```

### Configuration

1. Set up environment variables:
```bash
# .env file
GOOGLE_API_KEY=your-gemini-api-key
```

2. Run the application:
```bash
python main.py
```

The server will start at `http://127.0.0.1:8082`

### API Endpoints

#### Root Endpoint
- `GET /`: Lists available tools and server status

#### Process Endpoint
- `POST /process/`: Processes natural language commands
  - Input: JSON with `query` field
  - Output: Processed command result


### Integration Points
1. **Google Gemini AI**
   - Natural language processing
   - Command interpretation
   - Tool selection

2. **MCP Server**
   - Tool execution
   - State management
   - Event handling

3. **Frontend**
   - Command reception
   - Response formatting
   - State updates



<hr>
## MCP Server Directory Structure

### Services Overview

The `mcp-server` directory contains the tool management and event handling services:

```
mcp-server/
├── main.py             # FastMCP server implementation
├── pyproject.toml      # Project metadata and dependencies
└── uv.lock            # UV dependency lock file
```

### Core Components

**FastMCP Server** (`main.py`)
   - Manages tool definitions for device control
   - Handles Server-Sent Events (SSE)
   - Provides these tool categories:
     - Device State Tools
     - Fan Control Tools
     - Light Control Tools
     - Thermostat Control Tools


### Features
- Tool-based device control
- Real-time event handling via SSE
- Async request processing
- Integration with Backend API
- Error management and reporting

### Installation with UV

Same as the MCP Client, just change the directory to `mcp-server`.
then Run the server:
```bash
python main.py
```

The server will start at `http://127.0.0.1:8081`

### Available Tools

1. **Device State Tools**
   - `devices_state`: Get state of all devices

2. **Fan Tools**
   - `create_fan`: Create new fan device
   - `update_fan`: Update fan state
   - `delete_fan`: Remove fan device

3. **Light Tools**
   - `create_light`: Create new light device
   - `update_light`: Update light state
   - `delete_light`: Remove light device

4. **Thermostat Tools**
   - `create_thermostat`: Create new thermostat device
   - `update_thermostat`: Update thermostat value
   - `delete_thermostat`: Remove thermostat device

### Integration Points

1. **Backend API**
   - Communicates with device endpoints
   - Manages device states
   - Handles CRUD operations

2. **MCP Client**
   - Receives tool definitions
   - Processes tool invocations
   - Handles event streams

### Error Handling

- Connection error management
- Request validation
- Response error handling
- Tool execution error handling


<hr>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request