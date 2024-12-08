from fastapi import FastAPI, WebSocket
from datetime import datetime

# Tworzymy instancję FastAPI
app = FastAPI()

# Lista logów w pamięci
logs = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Endpoint WebSocket do odbierania i przechowywania logów.
    """
    await websocket.accept()
    try:
        while True:
            # Odbieramy dane od klienta
            data = await websocket.receive_text()
            # Tworzymy log z czasem i wiadomością
            log = {"timestamp": datetime.now().isoformat(), "message": data}
            logs.append(log)
            # Wysyłamy potwierdzenie do klienta
            await websocket.send_text(f"Log zapisany: {data}")
    except Exception as e:
        print(f"Błąd WebSocket: {e}")
    finally:
        await websocket.close()

@app.get("/logs")
def get_logs():
    """
    Endpoint do pobierania logów HTTP.
    """
    return logs

@app.get("/")
def root():
    """
    Prosty endpoint testowy.
    """
    return {"message": "Serwer działa!"}
