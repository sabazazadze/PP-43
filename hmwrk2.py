prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}

orders = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("ლუკა", "ლეპტოპი", 1),
    ("ლუკა", "მონიტორი", 5),
]

spent = {}
failed = set()
revenue = 0

for name, product, qty in orders:
    if product not in prices:
        print(f"{name}: '{product}' არ იყიდება")
        failed.add(name)
    elif stock[product] < qty:
        print(f"{name}: {product} — მარაგში მხოლოდ {stock[product]} ცალია")
        failed.add(name)
    else:
        stock[product] -= qty
        total = prices[product] * qty
        spent[name] = spent.get(name, 0) + total
        revenue += total
        print(f"{name}: {product} x{qty} = {total} ლარი")

print("--- ანგარიში ---")
for name, amount in spent.items():
    print(f"{name}: {amount} ლარი")

print(f"შემოსავალი: {revenue} ლარი")

sold_out = []
for product, left in stock.items():
    if left == 0:
        sold_out.append(product)

print(f"ამოიწურა: {sorted(sold_out)}")
print(f"წარუმატებელი შეკვეთა ჰქონდათ: {sorted(failed)}")