import asyncio
import logging
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from api.routes.base_route import api_router
from api.routes.mcp_routes import run_mcp_server

logger = logging.getLogger(__name__)


def build_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    # Use BASE_PATH from Kubernetes deployment, fallback to ROOT_PATH

    # Create FastAPI app
    app = FastAPI(
        title="Sample MCP API",
        lifespan=lifespan
    )

    # Include mcp router
    app.include_router(
        api_router,
        tags=['Bug Free pancake']
    )

    return app


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage FastAPI app lifespan (startup and shutdown)."""
    # Startup

    logger.info("Starting MCP server task...")
    asyncio.create_task(run_mcp_server())
    


    yield

    # Shutdown
    logger.info("Shutting down MCP server...")
