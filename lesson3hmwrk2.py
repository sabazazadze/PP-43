card = "4111222233334444"
phone = "599123456"
# print("შენიღბული:", "*" * 12 + card[-4:])
print("შენიღბული:", "*" * 4 + " " + "*" * 4 + " " + "*" * 4 + " " + card[-4:])
print("პირველი 4 ციფრი",card[0:4])
print("ციფრების რაოდენობა:", len(card))
print("შებრუნებული:", card[::-1])
phone1 = phone[:3]
phone2 = phone[3:5]
phone3 = phone[5:7]
phone4 = phone[7:9]
new_phone = phone1 + " " + phone2 + " " + phone3 + " " + phone4
print(new_phone)
