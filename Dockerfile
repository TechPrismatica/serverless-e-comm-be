FROM python:3.12-slim-bookworm

WORKDIR /app

RUN pip install uv && uv virtualenv venv && uv venv

COPY requirements.txt .

RUN uv pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
