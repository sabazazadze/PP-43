import json
import requests

FILE_NAME = "jokes.json"


def load_history():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_history(history):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print("ფაილში ჩაწერა ვერ მოხერხდა:", e)


def get_joke(category="Any"):
    url = f"https://v2.jokeapi.dev/joke/{category}?safe-mode"
    data = requests.get(url).json()
    if data["error"]:
        return None
    if data["type"] == "single":
        text = data["joke"]
    else:
        text = data["setup"] + " - " + data["delivery"]
    return {"category": data["category"], "joke": text}


while True:
    print("\n1. შემთხვევითი ხუმრობა")
    print("2. ხუმრობა კატეგორიით (Programming, Misc, Dark, Pun, Spooky, Christmas)")
    print("3. შენახული ხუმრობების ნახვა")
    print("4. ხუმრობის წაშლა")
    print("0. გასვლა")
    choice = input("არჩევანი: ")

    if choice == "1" or choice == "2":
        if choice == "1":
            joke = get_joke()
        else:
            joke = get_joke(input("კატეგორია: ").capitalize())

        if joke is None:
            print("ასეთი კატეგორია ვერ მოიძებნა")
        else:
            print("\n[" + joke["category"] + "]", joke["joke"])

            if input("შევინახო? (y/n): ") == "y":
                history = load_history()
                history.append(joke)
                save_history(history)
                print("შენახულია")

    elif choice == "3":
        history = load_history()
        if not history:
            print("შენახული ხუმრობები არ არის")
        for i, j in enumerate(history):
            print(i + 1, "[" + j["category"] + "]", j["joke"])

    elif choice == "4":
        history = load_history()
        if not history:
            print("შენახული ხუმრობები არ არის")
            continue
        for i, j in enumerate(history):
            print(i + 1, j["joke"])
        try:
            num = int(input("რომელი წავშალო (ნომერი): "))
            history.pop(num - 1)
            save_history(history)
            print("წაშლილია")
        except (ValueError, IndexError):
            print("არასწორი ნომერი")

    elif choice == "0":
        break
