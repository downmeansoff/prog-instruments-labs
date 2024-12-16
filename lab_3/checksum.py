import csv
import json
import hashlib
import re
import os
from typing import List, Dict

"""
В этом модуле обитают функции, необходимые для автоматизированной проверки результатов ваших трудов.
"""

# Регулярные выражения для валидации
VALIDATION_RULES = {
    "email": r"^[a-z0-9]+(?:[._][a-z0-9]+)*\@[a-z]+(?:\.[a-z]+)+$",
    "http_status_message": r"^\d{3} [A-Za-z ]+$",
    "snils": r"^\d{11}$",
    "passport": r"^\d{2}\s\d{2}\s\d{6}$",
    "ip_v4": r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?){4}$",
    "longitude": r"^\-?(180|1[0-7][0-9]|\d{1,2})\.\d+$",
    "hex_color": r"^\#[0-9a-fA-F]{6}$",
    "isbn": r"^\d+-\d+-\d+-\d+(?:-\d+)?$",
    "locale_code": r"^[a-z]{2,3}(-[a-z]{2})?$",
    "time": r"^(2[0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]\.\d{6}$",
}

def validate_row(row: Dict[str, str]) -> List[str]:
    """
    Проверяет строку на валидность по заданным правилам.

    :param row: Словарь с данными строки
    :return: Список имен полей с ошибками валидации
    """
    invalid_fields = []
    for field, value in row.items():
        pattern = VALIDATION_RULES.get(field)
        if pattern and not re.match(pattern, value):
            invalid_fields.append(field)
    return invalid_fields

def process_csv(file_path: str) -> List[int]:
    """
    Обрабатывает CSV-файл и возвращает номера строк с ошибками валидации.

    :param file_path: Путь к CSV-файлу
    :return: Список номеров строк с ошибками
    """
    invalid_rows = []
    with open(file_path, newline='', encoding='utf-16') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row_number, row in enumerate(reader):
            invalid_fields = validate_row(row)
            if invalid_fields:
                invalid_rows.append(row_number)
    return invalid_rows

def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет md5 хеш от списка целочисленных значений.

    :param row_numbers: список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()

def serialize_result(variant: int, checksum: str, output_dir: str) -> None:
    """
    Метод для сериализации результатов лабораторной.

    :param variant: номер вашего варианта
    :param checksum: контрольная сумма, вычисленная через calculate_checksum()
    :param output_dir: директория для сохранения результата
    """
    result = {
        "variant": variant,
        "checksum": checksum
    }
    result_path = os.path.join(output_dir, 'result.json')
    with open(result_path, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

def main(csv_file_path: str, variant_number: int) -> None:
    """
    Основная функция для обработки CSV и сохранения результатов.

    :param csv_file_path: Путь к CSV-файлу
    :param variant_number: номер вашего варианта
    """
    # Обработка CSV файла
    invalid_row_numbers = process_csv(csv_file_path)
    
    # Вычисляем контрольную сумму
    checksum = calculate_checksum(invalid_row_numbers)
    
    # Получаем директорию для сохранения результата
    output_directory = os.path.dirname(csv_file_path)
    
    # Заполняем результат
    serialize_result(variant_number, checksum, output_directory)

if __name__ == "__main__":
    csv_file_path = 'C:/Users/glebo/Desktop/lab1/prog-instruments-labs/lab_3/sariant73.csv'
    variant_number = 73
    main(csv_file_path, variant_number)
