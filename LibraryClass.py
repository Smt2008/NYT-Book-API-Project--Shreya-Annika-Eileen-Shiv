class Library:
  def __init__(self):
    self.holdDict = {}
    self.users = []
    self.libraryBooks = []

  def isCheckedOut(self, Book):
    if Book.checked_out == True:
      return "This book is checked out"
    else:
      return "This book is available"

  def addBooks(self, Book):
    self.libraryBooks.append(Book)

  def showBooks(self):
    return self.libraryBooks

  def searchBooksbyTitle(self, Title):
    searchedBooks = []
    for x in range(len(self.libraryBooks)):
      if self.libraryBooks[x].getTitle() == Title:
        searchedBooks.append(self.libraryBooks[x])
    return searchedBooks

  def searchBooksbyAuthor(self, Author):
    searchedBooks = []
    for x in range(len(self.libraryBooks)):
      if self.libraryBooks[x].getAuthor() == Author:
        searchedBooks.append(self.libraryBooks[x])
    return searchedBooks

  def addUser(self, User):
    users.append(User)

