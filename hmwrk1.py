sityva = input("შეიყვანეთ სიტყვა: ")
simbolo = input("რომელი სიმბოლო დავთვალოთ: ")
mtvleli = 0

for i in sityva:
    if i == simbolo:
        mtvleli += 1
        continue
print(f"სიმბოლო {simbolo} გვხვდება: {mtvleli} - ჯერ")