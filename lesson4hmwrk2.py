print("===გთხოვთ შეიყვანეთ მთელი რიცხვი===")
first_number = int(input("პირველი რიცხვი: "))
second_number = int(input("მეორე რიცხვი:"))
third_number = int(input("მესამე რიცხვი:"))

if first_number >= second_number and first_number >= third_number:
    print(f"უდიდესი რიცხვია: {first_number} ")
elif second_number >= first_number and second_number >= third_number:
    print(f"უდიდესი რიცხვია: {second_number} ")
elif third_number >= first_number and third_number >= second_number:
    print(f"უდიდესი რიცხვია: {third_number} ")