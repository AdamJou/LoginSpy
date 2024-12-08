from fastapi import FastAPI, HTTPException
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

@app.post("/logs")
def post_log(message: str):
    """
    Endpoint HTTP do dodawania nowego logu.
    """
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")
    add_log(message)
    return {"status": "success", "log": {"timestamp": datetime.now().isoformat(), "message": message}}

@app.get("/logs")
def get_logs():
    """
    Endpoint HTTP do pobierania logów.
    """
    return logs
