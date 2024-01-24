from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router as api_router_v1

from app.core.config import settings
def get_application():
    app = FastAPI(title=settings.PROJECT_NAME)

    @app.on_event("startup")
    async def on_startup():
        pass

    @app.on_event("shutdown")
    async def on_shutdown():
        pass

    @app.get("/")
    async def root():
        return {"message": f"{settings.PROJECT_NAME} is running!"}

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router_v1, prefix=settings.API_V1_STR)
    return app

app =  get_application()
