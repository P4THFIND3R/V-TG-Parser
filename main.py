from pyrogram import Client
from pyrogram.enums import MessageMediaType
from datetime import datetime, timedelta
import os
import webbrowser

from config import me, target, catalog_today, file_with_links, days, limit

app = Client("my_account")


async def main():
    async with app:
        print("Начинаю загрузку файлов в директорию: {0}".format(catalog_today))
        async for message in app.get_chat_history(target, limit=limit):
            if message.date < datetime.today() - timedelta(days=days):
                break
            match message.media:
                case MessageMediaType.VIDEO | MessageMediaType.DOCUMENT:
                    split = message.video.file_name.split('.') if message.video else message.document.file_name.split(
                        '.')
                    msg_ext = split[1]
                    msg_cap = message.caption if message.caption else split[0]

                    filename = msg_cap + '.' + msg_ext
                    print('Загрузка файла:', filename)
                    # await app.download_media(message, catalog_today + filename)
                case MessageMediaType.PHOTO:
                    await app.download_media(message, catalog_today)
                case MessageMediaType.WEB_PAGE:
                    with open(file_with_links, 'a', encoding='utf-8') as f:
                        f.write(message.text + '\n')
                    webbrowser.open_new_tab(message.web_page.url)
                case _:
                    if message.text and 'https' in message.text:
                        with open(file_with_links, 'a', encoding='utf-8') as f:
                            f.write(message.text + '\n')

    print("\033[32m----- Скачивание завершено! -----\033[0m")
    print()
    print(
        "Обратите внимание, что файлы, отправленные при помощи ссылки (ЯндексДиск, GoogleDrive), необходимо загрузить самостоятельно!")
    print("Для этого в открывшемся каталоге откройте текстовый документ 'Ссылки' и скачайте файлы!")
    os.system(r'start {0}'.format(catalog_today))


app.run(main())
