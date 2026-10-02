buy = float(input("შეიყვანეთ თანკა: "))
promo = input("პრომო-კოდი (თუ არ გაქვთ — Enter): ").strip().upper()

if buy >= 200 and promo == "VIP":
    print("🎁 VIP კოდი: დამატებით -5 ლარი ")
    print("ფასდაკლება: 20%")
    sale = buy * 0.2 + 5
    total = buy - sale
    print("გადასახდელი: ", total)
elif buy >= 200:
    print("ფასდაკლება: 20%")
    sale = buy * 0.2
    total = buy - sale
    print("გადასახდელი: ", total)
if buy >= 100 and buy<= 199.99 and promo == "VIP":
    print("🎁 VIP კოდი: დამატებით -5 ლარი ")
    print("ფასდაკლება: 10%")
    sale =buy * 0.1 + 5
    total = buy - sale
    print("გადასახდელი: ", total)
elif buy >= 100 and buy<= 199.99:
    print("ფასდაკლება: 10%")
    sale = buy * 0.1
    total = buy - sale
    print("გადასახდელი: ", total)
if buy >= 50 and buy <= 99.99 and promo == "VIP":
    print("🎁 VIP კოდი: დამატებით -5 ლარი ")
    print("ფასდაკლება: 5%")
    sale = buy * 0.05 + 5
    total = buy - sale
    print("გადასახდელი: ", total)
elif buy >= 50 and buy <= 99.99:
    print("ფასდაკლება: 5%")
    sale = buy * 0.05
    total = buy - sale
    print("გადასახდელი: ", total)
if buy <= 49.99 and promo == "VIP":
   print("🎁 VIP კოდი: დამატებით -5 ლარი ")
   print("ფასდაკლება: 0%")
   sale = 5
   total = buy - sale
   print("გადასახდელი: " , total)
elif buy <= 49.99:
    print("ფასდაკლება: 0%")
    total = buy
    print("გადასახდელი: ", total)