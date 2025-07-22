import logging

from fastmcp import FastMCP

mcp = FastMCP(name="SampleMCPService")

logger = logging.getLogger(__name__)


async def run_mcp_server():
    """Run the MCP server in the background."""

    try:
        await mcp.run_async(
            transport="streamable-http",
            host="localhost",
            port=8001
        )

    except Exception as e:
        logger.error(f"Error starting MCP server: {e}")
        raise


@mcp.tool
def greet(name: str) -> str:
    """A simple tool that greets the user."""
    return f"Hello, {name}!"


@mcp.tool(name="get_timesheet", description="Get the timesheet")
async def get_timesheet() -> str:
    # return a sample time json data
    return """
    {
        "2023-10-01": {
            "project": "Project A",
            "hours": 8,
            "description": "Worked on feature X"
        },
        "2023-10-02": {
            "project": "Project B",
            "hours": 6,
            "description": "Bug fixing"
        }
    }
    """