class Book:

    def __init__(self, title, author, numCopies, numCopiesLoaned):
        self.title = title
        self.author = author
        self.numCopies = numCopies
        self.numCopiesLoaned = numCopiesLoaned

    def prestamo(self):
        if self.numCopies > 0:
            self.numCopies -= 1
            self.numCopiesLoaned += 1
            return True
        return False

    def devolucion(self):
        if self.numCopiesLoaned > 0:
            self.numCopiesLoaned -= 1
            self.numCopies += 1
            return True
        return False
    
    def __str__(self): 
        return f"Title: {self.title}, author: {self.author}, number of copies: {self.numCopies}, number of copies loaned: {self.numCopiesLoaned}"

    def __eq__(self, other): 
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): 
        return self.author < other.author
