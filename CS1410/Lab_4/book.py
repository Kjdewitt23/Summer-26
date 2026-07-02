"""
Complete Lab 4 and update the following information:

Author: Kollin DeWitt
Date: 7/2/2026
"""
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def __str__(self):
        return f"{self._title} by {self._author}"
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        elif title == "":
            raise ValueError("Title must not be empty")
        else:
            self._title = title
    
    title = property(get_title, set_title)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        elif author == "":
            raise ValueError("Author must not be empty")
        else:
            self._author = author

    @property
    def description(self):
        return f"{self._title} was written by {self._author}"

def main():
    my_book = Book("Book", "Author")
    my_book.title = "The Stormlight Archive"
    my_book.author = "Brandon Sanderson"
    print(my_book)
    print(my_book.description)
    #my_book.description = f"{my_book.title} is a book written by {my_book.author}"
    
if __name__ == "__main__":
    main()