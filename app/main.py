from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.routers import main_router
from app.settings import DATABASE_CONFIG

app = FastAPI(
    title="Сервис по расчёту стоимости страхования",
    description="Расчёт стоимости страхования в зависимости от типа груза"
    "и объявленной стоимости (ОС)"
)
app.include_router(main_router)


register_tortoise(
    app=app,
    config=DATABASE_CONFIG
)
