from dotenv import load_dotenv
from scripts.core.services.user import user_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(user_router)

# from scripts.utils import preflight

    

# preflight.run()
