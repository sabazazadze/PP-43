print("=== სტუდენტის შეფასების სისტემა ===")

try:


    student_name = input("შეიყვანეთ სტუდენტის სახელი: ").strip()
    initial = student_name[0]

    student_grade = int(input("შეიყვანეთ მიღებული ქულა: "))
    student_max_grade = int(input("შეიყვანეთ მაქსიმალური ქულა: "))

    percent =  student_grade / student_max_grade * 100
except IndexError:
    print("❌ სახელი ცარიელი ვერ იქნება ")
except ValueError:
    print("❌ ქულები მთელი რიცხვებით ჩაწერეთ")
except ZeroDivisionError:
    print("❌ მაქსიმალური ქულა 0 ვერ იქნება ")
else:

    if student_grade < 0 or student_grade > student_max_grade:
        print("❌ ქულა არასწორ დიაპაზონშია")
    else:
        if percent >= 91:
            grade = "A"
        elif percent >= 81:
            grade = "B"
        elif percent >= 71:
            grade = "C"
        elif percent >= 61:
            grade = "D"
        elif percent >= 51:
            grade = "E"
        elif percent >= 41:
            grade = "FX"
        elif percent <= 40:
            grade = "F"

        print(f"{initial}. {student_name} - {percent} - შეფასება: {grade}")
finally:
    print("შეფასების სისტემამ მუშაობა დაასრულა")