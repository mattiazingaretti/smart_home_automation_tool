# Smart Home Automation Tool

A distributed system for managing and controlling smart home devices through natural language processing using Google's Gemini AI.

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
- Node.js and npm (for frontend)

## Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart_home_automation_tool.git
cd smart_home_automation_tool
```

2. Set up environment variables:

Backend (.env):
```plaintext
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
```

MCP Client (.env):
```plaintext
GOOGLE_API_KEY=your-gemini-api-key
```

## Installation

1. Backend API:
```bash
cd app
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. MCP Server:
```bash
cd mcp-server
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. MCP Client:
```bash
cd mcp-client
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

4. Gradio Frontend:
```bash
cd gradio_fe
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

1. Start the PostgreSQL database

2. Start the Backend API:
```bash
cd app
python main.py
```

3. Start the MCP Server:
```bash
cd mcp-server
python main.py
```

4. Start the MCP Client:
```bash
cd mcp-client
python main.py
```

5. Start the Gradio Frontend:
```bash
cd gradio_fe
python main.py
```

Access the web interface at: http://localhost:7860

## API Endpoints

### Backend API (Port 8080)

- `GET /devices/state` - Get all device states
- `POST /light/lights/` - Create a light device
- `PUT /light/lights/{name}/` - Update light state
- `POST /fan/fans/` - Create a fan device
- `PUT /fan/fans/{name}/` - Update fan state
- `POST /thermostat/thermostats/` - Create a thermostat device
- `PUT /thermostat/thermostats/{name}/` - Update thermostat value

### MCP Client API (Port 8082)

- `POST /process` - Process natural language commands
- `GET /` - List available tools

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request