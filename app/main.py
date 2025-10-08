from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.DESCRIPTION,
)

@app.get("/health", tags=["Health"], summary="Health Check Endpoint")
async def health():
    payload = {
        "status": "ok",
        "app": settings.APP_NAME,
        "app": settings.APP_VERSION
    }
    return JSONResponse(content=payload)

if __name__ == "__main__":
    # This block allows running the app as: python -m app.main
    # It uses uvicorn programmatically — convenient for local dev or container CMD.
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=9000, reload=True)