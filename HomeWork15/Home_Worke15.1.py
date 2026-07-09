import csv
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent

homework_dir = BASE_DIR
file1_path = homework_dir / "first.csv"
file2_path = homework_dir / "second.csv"
output_path = homework_dir / "result_Zabolotnyi.csv"

unique_rows = set()
header = None

def read_csv(file_path):
    global header
    if not file_path.exists():
        print(f"Файл не знайдено: {file_path}")
        return

    with open(file_path, mode='r') as f:
        reader = csv.reader(f)
        try:
            file_header = next(reader)
            if not header:
                header = file_header
        except StopIteration:
            return

        for row in reader:
            unique_rows.add(tuple(row))

read_csv(file1_path)
read_csv(file2_path)


with open(output_path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)


    if header:
        writer.writerow(header)


    for row in unique_rows:
        writer.writerow(row)

print(f"Завдання виконано! Чистий результат збережено в: {output_path}")