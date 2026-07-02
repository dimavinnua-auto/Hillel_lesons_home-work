from pathlib import Path
import json
import logging

BASE_DIR = Path(__file__).resolve().parent

homework_dir = BASE_DIR

file1_path = homework_dir / "1.json"
file2_path = homework_dir / "2.json"
file3_path = homework_dir / "3.json"
file4_path = homework_dir / "4.json"
og_file_path = homework_dir / "result2_Zabolotnyi.csv"

# 👇 Этой строки не хватало
log_file_path = homework_dir / "result2_Zabolotnyi.py"

logger = logging.getLogger("json_validator")
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


json_dir = BASE_DIR
files_to_check = ["1.json", "2.json", "3.json", "4.json"]


for file_name in files_to_check:
    file_path = json_dir / file_name


    if not file_path.exists():
        print(f"Помилка: Файл {file_name} не знайдено у папці {json_dir}")
        continue

    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            # Спроба десеріалізації (читання) JSON
            json.load(f)
            print(f"Файл {file_name} -> ВАЛІДНИЙ")

    except (json.JSONDecodeError, UnicodeDecodeError) as e:

        logger.error(f"Файл невалідний: {file_name}. Деталі помилки: {e}")
        print(f"Файл {file_name} -> НЕВАЛІДНИЙ (інформацію записано в лог)")

print(f"\nПеревірку завершено. Лог помилок збережено в: {log_file_path}")