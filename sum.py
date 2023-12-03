# TODO решите задачу
import json

def task(INPUT_FILENAME) -> float:
    with open(INPUT_FILENAME) as file:
        lines = json.load(file)
    sum = 0
    for line in lines:
        sum += line.get("score") * line.get("weight")
    return round(sum, 3)

print(task("input.json"))
