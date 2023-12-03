# TODO импортировать необходимые молули
import csv
import json

def task(INPUT, OUTPUT) -> None:
   # TODO считать содержимое csv файла

   # TODO Сериализовать в файл с отступами равными 4
    with open(INPUT) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', lineterminator='\n')
        json_data = []
        for row in csv_reader:
            json_data.append(row)
    with open(OUTPUT, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    with open(OUTPUT) as file:
        for line in file:
            print(line, end="")

if __name__ == '__main__':
    # Нужно для проверки
    task("input.csv", "output.json")