import requests
import time

#  ________  _______   ________           ________  ________  _____ ______   _____ ______   ___  ___  ________   ___  _________    ___    ___ 
# |\_____  \|\  ___ \ |\   ___  \        |\   ____\|\   __  \|\   _ \  _   \|\   _ \  _   \|\  \|\  \|\   ___  \|\  \|\___   ___\ |\  \  /  /|
#  \|___/  /\ \   __/|\ \  \\ \  \       \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \  \\\__\ \  \ \  \\\  \ \  \\ \  \ \  \|___ \  \_| \ \  \/  / /
#      /  / /\ \  \_|/_\ \  \\ \  \       \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \\|__| \  \ \  \\\  \ \  \\ \  \ \  \   \ \  \   \ \    / / 
#     /  /_/__\ \  \_|\ \ \  \\ \  \       \ \  \____\ \  \\\  \ \  \    \ \  \ \  \    \ \  \ \  \\\  \ \  \\ \  \ \  \   \ \  \   \/  /  /  
#    |\________\ \_______\ \__\\ \__\       \ \_______\ \_______\ \__\    \ \__\ \__\    \ \__\ \_______\ \__\\ \__\ \__\   \ \__\__/  / /    
#     \|_______|\|_______|\|__| \|__|        \|_______|\|_______|\|__|     \|__|\|__|     \|__|\|_______|\|__| \|__|\|__|    \|__|\___/ /     
#                                                                                                                                \|___|/      
# HOW TO GET YOUR TOKEN?
#1. Open Discord in your browser (e.g. Chrome).
#Go to https://discord.com/app.
#
#2. Open developer tools (F12) > Network tab.
#
#3. In the search box type science (or just filter by messages, typing, etc.).
#
#4. Refresh the page (F5) and click on a channel.
#
#5. Find a request like science, messages, typing, read-state, track, etc. Click on it.
#
#6. Go to Headers > Request Headers.
#
#7. Find Authorization - that's where your token will be.
#It looks something like this:
#
#Authorization: YOUR ACCOUNT TOKEN
#
#Save it somewhere safe. Treat it like a password.

# HOW TO GET A CHAT ID?
#1. Open Discord.
#
#2. Enable Developer Mode in Settings (Settings/Advanced (in the "Application Settings" section))
#
#3. Right-click on a chat (server channel, DM, group, etc.)
#
#4. Click "Copy Channel ID"



TOKEN = "TWÓJ TOKEN KONTA" # Zmień na swój token
CHANNEL_ID = "ID CZATU"
MESSAGE = "WIADOMOŚĆ" # Zmień na swoją wiadomość
CZAS = 1 # Zmień na swój (w minutach)

headers = {
    "Authorization": TOKEN,  # Uwaga! Użycie selfbota może skutkować banem
    "Content-Type": "application/json"
}

def send_message():
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    json = {"content": MESSAGE}
    response = requests.post(url, headers=headers, json=json)
    print(f"Status: {response.status_code} | Treść: {response.text}")

while True:
    send_message()
    time.sleep(CZAS * 60)
