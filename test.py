from pyrogram import Client
from pyrogram.enums import MessageMediaType
from datetime import datetime, timedelta

from config import me, target, catalog_today, file_with_links, stocks_target

app = Client("my_account")

limit = 10
offset = 0
path = "C:\\Users\\PATHFIND3R\\Documents\\stocks\\"


async def main():
    async with app:
        async for message in app.get_chat_history(stocks_target, limit=limit, offset=offset):
            if message.media in (MessageMediaType.DOCUMENT, MessageMediaType.VIDEO):
                filename = message.video.file_name if message.video else message.document.file_name
                print('Загрузка файла:', filename)
                await app.download_media(message, path + filename)


app.run(main())
