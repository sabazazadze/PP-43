orders = [
    ("ხაჭაპური", 2, 12.5),
    ("ლობიანი", 1, 7.0),
    ("ლიმონათი", 3, 3.5),
    ("ხინკალი", 20, 1.2),
    ("ჩაი", 2, 2.5),
]

revenue = sum(qty * price for name, qty, price in orders)
items_count = sum(qty for name, qty, price in orders)
has_big_order = any(qty >= 10 for name, qty, price in orders)
biggest_line = max(qty * price for name, qty, price in orders)
first_cheap = next((name for name, qty, price in orders if price < 3), None)
first_very_cheap = next((name for name, qty, price in orders if price < 1), "ასეთი ვერ მოიძებნა"  )
several = ", ".join(name for name, qty, price in orders if qty > 1)
expensive_names = tuple(name for name, qty, price in orders if price > 5)

print("შემოსავალი:", round(revenue, 2), "₾")
print("ერთეულები:", items_count)
print("დიდი შეკვეთა (10+)?", has_big_order)
print("ყველაზე დიდი ხაზი:", biggest_line, "₾")
print("პირველი 3 ₾-ზე იაფი:", first_cheap)
print("პირველი 1 ₾-ზე იაფი:", first_very_cheap)
print("რამდენიმე ცალი:", several)
print(expensive_names)