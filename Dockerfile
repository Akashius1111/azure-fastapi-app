# Dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn httpx

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]