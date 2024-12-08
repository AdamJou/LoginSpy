from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

# Tworzenie instancji FastAPI
app = FastAPI()

# Lista logów
logs = []

def add_log(message: str):
    """
    Funkcja do dodawania logów do listy.
    """
    log = {"timestamp": datetime.now().isoformat(), "message": message}
    logs.append(log)

# Model do walidacji danych przesyłanych w formacie JSON
class LogEntry(BaseModel):
    message: str

@app.post("/logs")
def post_log(log_entry: LogEntry):
    """
    Endpoint HTTP do dodawania nowego logu.
    """
    add_log(log_entry.message)
    return {"status": "success", "log": {"timestamp": datetime.now().isoformat(), "message": log_entry.message}}

@app.get("/logs")
def get_logs():
    """
    Endpoint HTTP do pobierania logów.
    """
    return logs

@app.get("/")
def root():
    """
    Testowy endpoint.
    """
    return {"message": "Serwer działa!"}
