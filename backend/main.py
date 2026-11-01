from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="AI-Powered Business Operations Agent")
app.include_router(router)
