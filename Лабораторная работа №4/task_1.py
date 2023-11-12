import json

def task() -> float:
    with open("input.json", "r") as file:
        data = json.load(file)
        result = [i["score"]*i["weight"] for i in data]
        return round(sum(result),3)


print(task())
