import uvicorn
from dotenv import load_dotenv

from scripts.config import ServiceConfig

if __name__ == "__main__":
    load_dotenv()

    uvicorn.run("main:app", host=ServiceConfig.HOST, port=ServiceConfig.PORT)
