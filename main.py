from fastapi import FastAPI

import api


tasg_metadata = [
    {
        "name": "users",
        "description": "Создание, редактирование, удаление и просмотр пользователей",
    },
]

app = FastAPI(
    title="Address book",
    description="Тестовое приложение 'Адрессная книга'",
    openapi_tags=tasg_metadata
)
app.include_router(api.router)