from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from datetime import datetime
import requests
import asyncio

# Tworzenie instancji FastAPI
app = FastAPI()

# Zmienna przechowująca tylko jeden najnowszy log
latest_log = None

def set_latest_log(message: str):
    global latest_log
    latest_log = {
        "id": str(uuid4()),  # Generuje unikalne ID
        "timestamp": datetime.now().isoformat(),
        "message": message,
    }

# Model do walidacji danych przesyłanych w formacie JSON
class LogEntry(BaseModel):
    message: str

@app.post("/logs")
def post_log(log_entry: LogEntry):
    """
    Endpoint HTTP do dodawania nowego logu.
    """
    set_latest_log(log_entry.message)
    return {"status": "success", "log": {"timestamp": datetime.now().isoformat(), "message": log_entry.message}}

@app.get("/logs")
def get_logs():
    if latest_log is None:
        return {"message": "No logs available."}
    return latest_log

@app.get("/")
def root():
    """
    Testowy endpoint.
    """
    return {"message": "Serwer działa!"}

async def keep_alive():
    """
    Background task to keep the service active by pinging its own URL.
    """
    url = "https://loginspy.onrender.com/"  # Replace with your actual Render app URL
    while True:
        try:
            response = requests.get(url)
            print(f"Keep-alive ping sent. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error in keep-alive ping: {e}")
        await asyncio.sleep(840)  # Ping every 14 minutes (840 seconds)

@app.on_event("startup")
async def startup_event():
    """
    Runs on application startup and triggers the keep-alive task.
    """
    # Usuń tymczasowo keep-alive
    asyncio.create_task(keep_alive())
    print("Application startup complete.")
