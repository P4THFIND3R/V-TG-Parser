from datetime import datetime

# ID информационного канала экрана
target = -1001989999005
# ID канала со стоками
stocks_target = -1001875882937
me = "me"
# За какой промежуток времени скачиваем файлы (в днях)
days = 6
# Максимальное количество сообщений просматриваемых программой
limit = 500

# stuff
today = datetime.today().strftime("%d.%m")

# files and directories
catalog_today = f"C:\\Users\\PATHFIND3R\\Documents\\{today}\\"
txt_file_name = "Ссылки.txt"
file_with_links = catalog_today + txt_file_name
