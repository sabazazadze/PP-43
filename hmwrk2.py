# mcdeloba adzin
# paroli = "python2026"
#
# while True:
#     monacemi = input("შეიყვანეთ პაროლი: ")
#     if monacemi == paroli:
#         print("წვდომა დაშვებულია")
#         break
#     elif monacemi != paroli:
#         print("პაროლი არასწორია, დაგრჩათ 2 მცდელობა")
#         monacemi = input("შეიყვანეთ პაროლი: ")
#         if monacemi == paroli:
#             print("წვდომა დაშვებულია")
#             break
#         elif monacemi != paroli:
#             print("პაროლი არასწორია, დაგრჩათ 1 მცდელობა")
#             monacemi = input("შეიყვანეთ პაროლი: ")
#             if monacemi == paroli:
#                 print("წვდომა დაშვებულია")
#                 break
#             else:
#                 print("ანგარიში დაბლოკილია")






paroli = "python2026"
mcdeloba = 3

while mcdeloba > 0:
    monacemi = input("შეიყვანეთ პაროლი: ")
    if monacemi == "":
        mcdeloba -= 1
        print(f"ცარიელი პაროლი დაგრჩა {mcdeloba} მცდელობა. ")
        continue
    if monacemi == paroli:
        print("პაროლი სწორია.")
        break
    if monacemi != paroli:
        mcdeloba -= 1
        print(f"პაროლი არასწორია დაგრჩა {mcdeloba} მცდელობა.")
else:
    print("ანგარიში დაბლოკილია")
