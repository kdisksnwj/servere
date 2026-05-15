import requests
import time
import os

URL = "https://chat-server-1xnj.onrender.com/status"

while True:
    try:
        r = requests.get(URL, timeout=5)
        data = r.json()

        online = data.get("online", 0)

        os.system("cls")  # Windows clear screen
        print("🔵 Serveur connecté")
        print(f"👥 Utilisateurs en ligne : {online}")

    except Exception as e:
        os.system("cls")
        print("🔴 Impossible de contacter le serveur")
        print("Erreur:", e)

    time.sleep(2)
