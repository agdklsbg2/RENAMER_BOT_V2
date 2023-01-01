from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5865662663:AAG0n3-YPuGL0JKaqDIq_pM5LZHRqbEILX4")

API_ID = int(os.environ.get("API_ID", "24188340"))

API_HASH = os.environ.get("API_HASH", "176df5b4c6d99b4e5b3f9be2baa8f6e9")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
