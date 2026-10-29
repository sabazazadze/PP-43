class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"{self.title} — {self.author}, {self.pages} გვ.")


book1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 250)
book2 = Book("კადმოსის მემკვიდრენი", "ჯემალ ქარჩხაძე", 320)
book3 = Book("ბახტრიონი", "ილია ჭავჭავაძე", 180)

book1.info()
book2.info()
book3.info()