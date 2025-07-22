from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the service is running.
    Returns a simple message indicating the service is healthy.
    """
    return {"status": "healthy"}