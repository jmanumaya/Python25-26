from book import Book

def main():
    book1 = Book("La leyenda de las tierras raras", "Folagor", 10, 0)
    book2 = Book("Entiende la Tecnología", "Nate Gentile", 20, 0)

    print(book1)
    print(book2)

    print("Success Operation") if book1.prestamo() else print("Operation Error")
    print(book1)

    print("Success Operation") if book1.devolucion() else print("Operation Error")
    print(book1)

    print(book1.__eq__(book2))
    print(book2.__lt__(book1))
main()