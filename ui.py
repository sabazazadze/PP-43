from bookmanager import BookManager

LINE = "=" * 50
THIN = "-" * 50


def print_menu():
    print()
    print(LINE)
    print("          წიგნების მენეჯერი")
    print(LINE)
    print(" 1. წიგნის დამატება")
    print(" 2. წიგნის ძებნა")
    print(" 3. წიგნის წაშლა")
    print(" 4. ყველა წიგნის ჩვენება")
    print(" 0. გასვლა")
    print(THIN)


def ask(prompt):
    return input(prompt).strip()


def handle_add(manager):
    title = ask("სათაური: ")
    author = ask("ავტორი: ")
    year = ask("გამოშვების წელი: ")
    book = manager.add_book(title, author, year)
    print(f"✔ დაემატა: {book}")


def handle_search(manager):
    title = ask("შეიყვანე სათაური (ან მისი ნაწილი): ")
    manager.search_book(title)


def handle_remove(manager):
    title = ask("წასაშლელი წიგნის სათაური: ")
    if manager.remove_book(title):
        print("✔ წიგნი წაიშალა.")
    else:
        print("✘ ასეთი წიგნი ვერ მოიძებნა.")


def run():
    manager = BookManager()
    actions = {
        "1": handle_add,
        "2": handle_search,
        "3": handle_remove,
        "4": lambda m: m.show_books(),
    }

    while True:
        print_menu()
        try:
            choice = ask("აირჩიე მოქმედება: ")

            if choice == "0":
                print("ნახვამდის!")
                break

            action = actions.get(choice)
            if action is None:
                print("✘ არასწორი არჩევანი. შეიყვანე 0-დან 4-მდე.")
                continue

            action(manager)

        except ValueError as e:
            print(f"✘ შეცდომა: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nპროგრამა შეწყდა. ნახვამდის!")
            break
        except Exception as e:
            print(f"✘ მოულოდნელი შეცდომა: {e}")
