EXTRA_PRICES = {"popcorn": 6, "cola": 3, "nachos": 7}

def book_tickets(movie, *seats, discount=0, **extras):
    valid_seats= list(filter(lambda s: len(s) >= 2  and s[0] in "ABCDE" and s[1:] .isdigit() and 1 <= int(s[1:]) <= 10, seats))
    prices = list(map(lambda s: 15 if s[0] in "AB" else 10, valid_seats))
    ticekts_total = sum(prices) * (1 - discount / 100)
    extras_total = sum(EXTRA_PRICES.get(name, 0) * qty for name, qty in extras.items())

    return {"movie" : movie, "seats" : valid_seats, "rejected" : len(seats) - len(valid_seats), "total" : round(ticekts_total + extras_total, 2)}



order1 = book_tickets("ოპენჰაიმერი", "A5", "C3", "Z1", "B12", "E10")
order2 = book_tickets("დიუნა", "B1", "B2", discount=20, popcorn=2, cola=2)
order3 = book_tickets("ინტერსტელარი", "D4", nachos=1)
order4 = book_tickets("ბარბი")

for order in [order1, order2, order3, order4]:
    print(f"{order['movie']}: ადგილები {order['seats']}, უარყოფილი: {order['rejected']}, სულ: {order['total']} ლარი")




