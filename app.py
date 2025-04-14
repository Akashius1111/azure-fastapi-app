from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Azure Web Service! Modus ETP"}

@app.get("/external")
async def call_external_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.publicapis.org/entries")
        return {"api_count": len(response.json()["entries"])}
