class Book:
    def __init__(self, title="GenericName", author="GenericAuthor", year=2000):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

war_and_peace = Book(title="Война и мир", author="Лев Николаевич Толстой", year=1863)
print(war_and_peace.get_info())
