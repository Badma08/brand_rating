import argparse
import csv
import sys
from reports.average_rating import average_rating_report
from tabulate import tabulate


def read_csv_files(file_paths):
    rows = []
    for path in file_paths:
        try:
            with open(path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    rows.append(row)
        except FileNotFoundError:
            print(f"Файл '{path}' не найден", file=sys.stderr)
        except Exception as e:
            print(f"Ошибка при чтении файла '{path}': {e}", file=sys.stderr)
    return rows

def main():
    parser = argparse.ArgumentParser(description="Генератор отчётов по рейтингам товаров")
    parser.add_argument("--files", nargs="+", required=True, help="Пути к CSV-файлам")
    parser.add_argument("--report", required=True, help="Тип отчёта")
    args = parser.parse_args()

    rows = read_csv_files(args.files)

    # Блок 1
    if args.report == "average-rating":
        report_data = average_rating_report(rows)
        print(tabulate(report_data, headers=["Бренд", "Средний рейтинг"], tablefmt="github"))
    else:
        print(f'{args.report} не существует')

    
if __name__ == "__main__":
    main()


