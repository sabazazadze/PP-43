import os

DATA_DIR = r"C:\Users\zazad\OneDrive\Desktop\pythoninvscode\data"
SCORES_PATH = os.path.join(DATA_DIR, "scores.txt")
PASSED_PATH = os.path.join(DATA_DIR, "passed.txt")


def save_scores(path: str, scores: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        for name, score in scores.items():
            file.write(f"{name}:{score}\n")


def add_score(path: str, name: str, score: int) -> None:
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{name}:{score}\n")


def read_scores(path: str) -> dict[str, int]:
    scores = {}
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            name, score = line.split(":")
            scores[name] = int(score)
    return scores

os.makedirs(DATA_DIR, exist_ok=True)

save_scores(SCORES_PATH, {"ნინო": 92, "გიორგი": 78, "ანა": 85})
add_score(SCORES_PATH, "დათო", 64)
add_score(SCORES_PATH, "მარიამი", 97)

with open(SCORES_PATH, encoding="utf-8") as file:
    print(file.read(), end="")

scores = read_scores(SCORES_PATH)
print(scores)

print("სტუდენტები:", len(scores))

average = sum(scores.values()) / len(scores)
print("საშუალო ქულა:", round(average, 1))

best_name = max(scores, key=scores.get)
print("საუკეთესო:", best_name, scores[best_name])

with open(PASSED_PATH, "w", encoding="utf-8") as file:
    for name, score in scores.items():
        if score >= 80:
            file.write(name + "\n")

passed = []
with open(PASSED_PATH, encoding="utf-8") as file:
    for line in file:
        passed.append(line.strip())
print("ჩააბარეს (80+):", passed)