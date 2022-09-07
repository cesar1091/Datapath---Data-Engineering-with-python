from fastapi import FastAPI
from routes.answer import answer

app = FastAPI(
    title="Datapath project API",
    openapi_tags=[{
        "name":"answer",
        "description":"answer routes"
    }]
)
app.include_router(answer)