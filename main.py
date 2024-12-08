from fastapi import FastAPI, WebSocket
from datetime import datetime

# Tworzenie instancji FastAPI
app = FastAPI()

# Przykładowe logi
logs = [
    {"timestamp": "2024-12-07T10:00:00", "message": "Komputer uruchomiony przez użytkownika Adam"},
    {"timestamp": "2024-12-07T15:30:00", "message": "Komputer uruchomiony przez użytkownika Kasia"},
    {"timestamp": "2024-12-08T08:00:00", "message": "Komputer uruchomiony przez użytkownika Piotr"},
]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket do odbierania logów.
    """
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            log = {"timestamp": datetime.now().isoformat(), "message": data}
            logs.append(log)
            await websocket.send_text(f"Log zapisany: {data}")
    except Exception as e:
        print(f"Błąd WebSocket: {e}")
    finally:
        await websocket.close()

@app.get("/logs")
def get_logs():
    """
    HTTP endpoint do pobierania logów.
    """
    return logs

@app.get("/")
def root():
    """
    Testowy endpoint.
    """
    return {"message": "Serwer działa!"}
