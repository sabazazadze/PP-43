import json


def save_json(path, data):
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


data = {"name": "ნინო", "scores": [90, 85], "pair": (1, 2)}
save_json("test.json", data)
result = load_json("test.json")
print(result)
print(type(result["pair"]))
print(load_json("არარსებული.json", default = {}))

with open("broken.json", "w", encoding="utf-8") as f:
    f.write('{"name": "ნინო",}')

print(load_json("broken.json", default="არასწორი ფაილი"))