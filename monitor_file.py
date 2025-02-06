import time

def monitor_file(filename, interval=5):
    """
    Моніторить файл та шукає слово "retry" в нових рядках.
    :param filename: Шлях до файлу для моніторингу.
    :param interval: Інтервал перевірки в секундах.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file.seek(0, 2)  # Переміщаємо курсор у кінець файлу
            position = file.tell()  # Запам'ятовуємо позицію курсора
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return

    print(f"Моніторинг файлу {filename}...")

    while True:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                file.seek(position)  # Повертаємо курсор на попередню позицію
                lines = file.readlines()
                position = file.tell()  # Оновлюємо позицію курсора

                for line in lines:
                    if 'retry' in line.lower():
                        print("Знайдено 'retry':", line.strip())
        except Exception as e:
            print("Помилка при читанні файлу:", e)

        time.sleep(interval)  # Затримка перед наступною перевіркою

# Виклик функції (замініть 'logfile.txt' на свій файл)
monitor_file('logfile.txt', interval=5)  #retry connection lost