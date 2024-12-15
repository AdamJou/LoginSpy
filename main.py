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
    """
    Funkcja do ustawiania najnowszego logu.
    """
    global latest_log
    latest_log = {"timestamp": datetime.now().isoformat(), "message": message}

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
    """
    Endpoint HTTP do pobierania najnowszego logu.
    """
    if latest_log is None:
        return {"message": "No logs available."}
    return latest_log

@app.get("/")
def root():
    """
    Testowy endpoint.
    """
    return {"message": "Serwer działa!"}



@app.on_event("startup")
async def startup_event():
    """
    Runs on application startup and triggers the keep-alive task.
    """
    # Usuń tymczasowo keep-alive
    # asyncio.create_task(keep_alive())
    print("Application startup complete.")
