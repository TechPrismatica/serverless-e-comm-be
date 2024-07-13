from fastapi import FastAPI

from scripts.core.services.user import user_router
from scripts.utils import preflight

preflight.run()


app = FastAPI()

app.include_router(user_router)
