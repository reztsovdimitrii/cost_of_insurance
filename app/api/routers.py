from fastapi import APIRouter

from app.api.endpoints import cargo_rate_router

main_router = APIRouter()
main_router.include_router(
    cargo_rate_router,
    prefix='/cargo_rate',
    tags=['Cargo Rate']
)
