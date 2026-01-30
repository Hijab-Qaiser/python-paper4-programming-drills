BookShelf = []  # empty string array


class book:
    def __init__(self, title, author, pages):
        self.title = title  # string variable
        self.author = author  # string variable
        self.pages = pages  # integer variable

    @property
    def GetTitle(self):
        return self.title

    @property
    def GetAuthor(self):
        return self.author

    @property
    def GetPages(self):
        return self.pages

    def IsLongBook(self):
        if self.pages > 300:
            return True
        return False


book_1 = book("Python Programming", "John Smith", 450)
book_2 = book("Web Design Basics", "Sarah Lee", 250)
book_3 = book("Data Structures", "Mike Chen", 520)

BookShelf.append(book_1)
BookShelf.append(book_2)
BookShelf.append(book_3)
LongBooks = 0  # integer variable
for count in range(len(BookShelf)):
    print(f"Title: {BookShelf[count].GetTitle}")
    if BookShelf[count].IsLongBook():
        LongBooks += 1

print(f"Number of long books: {LongBooks}")
