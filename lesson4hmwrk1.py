age = int(input("ასაკი: "))
parent = input("მშობელთან ერთად ხართ?(კი/არა): " ).strip()
with_parent = "კი"

if age <= 12:
    print("შესვლა აკრძალულია")
elif age >= 18 or (parent == with_parent):
    print("შესვლა დაშვებულია")
else:
    print("შესვლა აკრძალულია")