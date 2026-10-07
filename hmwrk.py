orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]
unique = []
for item in orders:
    if item not in unique:
        unique.append(item)
print(f"უნიკალური: {unique}")
freq = [(item, orders.count(item)) for item in unique]
print(f"სიხშირე: {freq}")
best_item, best_count = freq[0]
for item, count in freq:
    if count > best_count:
        best_item, best_count = item, count
print(f"ყველაზე პოპულალური: {best_item} ({best_count}-ჯერ)")
print(f"ბოლო სამი შეკვეთა: ", orders[-3:])