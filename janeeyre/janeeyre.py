import sys
from heapq import heappush, heappop

class Book:
    def __init__(self,name, pages) -> None:
        self.name = name
        self.pages = pages

    def __lt__(self, other):
        return self.name < other.name

def main():
    n,m,k = map(int, input().split())
    books = [Book("Jane Eyre", k)]

    future_books = []

    for _ in range(n):
        book = input().split("\"")
        name = book[1]
        pages = int(book[2])
        heappush(books, Book(name, pages))

    for _ in range(m):
        book = input().split("\"")
        time = int(book[0])
        name = book[1]
        pages = int(book[2])
        if name < 'Jane Eyre':
            future_books.append((time,Book(name, pages)))
    future_books.sort(key=lambda x: x[0])

    time = 0

    book_pointer = 0

    curr_book = None

    while curr_book == None or curr_book.name != 'Jane Eyre':
        curr_book = heappop(books)
        time += curr_book.pages
        if book_pointer < len(future_books) and time >= future_books[book_pointer][0]:
            heappush(books, future_books[book_pointer][1])
            book_pointer += 1

    print(time)




main()
