import requests
import platform
from datetime import datetime

def send_log():
    # Adres endpointu na serwerze
    url = "https://loginspy.onrender.com/logs"

    # Wiadomość z nazwą komputera i czasem uruchomienia
    message = f"Komputer '{platform.node()}' uruchomiony o {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Dane do wysłania jako JSON
    data = {"message": message}

    # Wysłanie loga do serwera
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Log wysłany pomyślnie!")
        else:
            print(f"Błąd przy wysyłaniu: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Błąd podczas wysyłania loga: {e}")

if __name__ == "__main__":
    send_log()
