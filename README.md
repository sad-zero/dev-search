# 🔍 Dev Search MCP Server

A powerful **Model Context Protocol (MCP)** server designed to search developer sites like GitHub, StackOverflow, and more. Built with [FastMCP](https://gofastmcp.com/) and Python 3.12, this server provides intelligent search capabilities for developer resources through a standardized MCP interface.

## ✨ Features

- 🚀 **Fast & Efficient**: Built on FastMCP framework for high-performance MCP operations
- 🔒 **Production-Ready**: Includes rate limiting, error handling, response caching, and comprehensive logging
- 🏗️ **Clean Architecture**: Dependency injection pattern with structured code organization
- 📊 **Structured Logging**: JSON-formatted logs with Unicode support (including Korean characters)
- 🐳 **Docker Support**: Containerized deployment with multi-stage builds
- ⚡ **Modern Tooling**: Uses `uv` for blazing-fast dependency management

## 📋 Prerequisites

- **Python**: 3.12 (3.13 not supported)
- **uv**: Latest version ([Installation Guide](https://github.com/astral-sh/uv))
- **Docker** (optional, for containerized deployment)

## 🛠️ Dependencies

### Core Dependencies

- **fastmcp** (>=2.14.1,<3): FastMCP framework for MCP server implementation
- **httpx** (>=0.28.1): Modern HTTP client for API requests
- **pydantic** (>=2.12.5): Data validation using Python type annotations
- **pydantic-settings** (>=2.12.0): Settings management using Pydantic models
- **dependency-injector** (>=4.48.3): Dependency injection framework
- **structlog** (>=25.5.0): Structured logging library
- **pyyaml** (>=6.0.3): YAML parser for configuration files
- **python-dotenv** (>=1.2.1): Environment variable management

### Development Dependencies

- **pytest** (>=9.0.2): Testing framework
- **pytest-cov** (>=7.0.0): Coverage plugin for pytest
- **pytest-mock** (>=3.15.1): Mocking utilities
- **pytest-asyncio** (>=1.3.0): Async test support

## 🚀 Local Deployment

### Step 1: Install uv

If you haven't installed `uv` yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or using pip:

```bash
pip install uv
```

### Step 2: Clone and Setup

```bash
git clone <repository-url>
cd dev-search
```

### Step 3: Configure Environment

Create a `.env` file in the project root:

```env
GITHUB_ENDPOINT=https://api.github.com
TOOL_CALL_LIMIT_PER_SECOND=10
ENVIRONMENT=local
```

### Step 4: Install Dependencies

Using `uv` to sync dependencies:

```bash
uv sync
```

This will:
- Create a virtual environment automatically
- Install all dependencies from `pyproject.toml`
- Use the lock file (`uv.lock`) for reproducible builds

### Step 5: Run the Server

```bash
uv run fastmcp run
```

The server will start on `http://0.0.0.0:8000` by default (configurable in `fastmcp.json`).

### Alternative: Run with Python

If you prefer to activate the virtual environment manually:

```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
fastmcp run
```

## 🐳 Docker Deployment

### Build the Docker Image

The Dockerfile uses a multi-stage build for optimized image size:

```bash
docker build \
  --build-arg ENVIRONMENT=dev \
  -t dev-search:latest \
  -f Dockerfile .
```

Replace `dev` with your target environment (`local`, `dev`, or `prod`).

### Run the Container

```bash
docker run -d \
  --name dev-search \
  -p 8000:8000 \
  -e PORT=8000 \
  dev-search:latest
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GITHUB_ENDPOINT` | GitHub API endpoint URL | - | Yes |
| `TOOL_CALL_LIMIT_PER_SECOND` | Rate limit for tool calls | - | Yes |
| `ENVIRONMENT` | Environment name (`local`, `dev`, `prod`) | - | Yes |

### FastMCP Configuration

The server behavior is configured in [fastmcp.json](/fastmcp.json):

### Logging Configuration

Logging is configured via [logging.yaml](/logging.yaml). The server uses structured JSON logging with Unicode support, making it easy to parse and analyze logs.

## 📁 Project Structure

```
dev-search/
├── src/
│   └── dev_search/
│       ├── __init__.py
│       ├── app.py              # Main MCP server entrypoint
│       ├── config.py           # Configuration and DI container
│       ├── inbound/            # Inbound adapters (Tool handlers)
│       └── outbound/           # Outbound adapters (external services)
├── logs/                       # Application logs
├── Dockerfile                  # Multi-stage Docker build
├── fastmcp.json               # FastMCP configuration
├── dev.fastmcp.json           # Development FastMCP config
├── pyproject.toml             # Project dependencies and metadata
├── uv.lock                    # Locked dependencies
├── logging.yaml               # Logging configuration
└── README.md                  # This file
```

## 🏗️ Architecture

The project follows a clean architecture pattern:

- **Inbound**: Handles incoming requests and adapts them to internal use cases
- **Outbound**: Interfaces with external services (GitHub, StackOverflow, etc.)
- **Dependency Injection**: Uses `dependency-injector` for loose coupling
- **Middleware Stack**: 
  - Error handling with traceback support
  - Request timing
  - Structured logging
  - Response caching
  - Rate limiting

## 📝 Development

### Running Tests

Run backend tests using:

```bash
uv run pytest
```

For protocol compliance and MCP inspector tests, you can use [ModelContextProtocol's Inspector](https://github.com/modelcontextprotocol/inspector):

```bash
npx @modelcontextprotocol/inspector test
```

Refer to the [official Inspector documentation](https://github.com/modelcontextprotocol/inspector) for setup and usage details.

### Adding Dependencies

```bash
uv add <package-name>
```

For development dependencies:

```bash
uv add --dev <package-name>
```

### Updating Dependencies

```bash
uv lock --upgrade
```

## 🔍 Usage Example

Once the server is running, you can connect to it using any MCP-compatible client. The server exposes tools for searching developer sites through the MCP protocol.

Example connection (using an MCP client):

```python
# Connect to the MCP server
# The server will be available at http://localhost:8000
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

**yeongro** - zeroro.yun@gmail.com

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Happy Searching! 🔍✨**