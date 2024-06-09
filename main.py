from dotenv import load_dotenv

from scripts.utils import preflight

if __name__ == "__main__":
    load_dotenv()

preflight.run()
