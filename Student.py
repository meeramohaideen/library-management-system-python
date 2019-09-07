#from Library import Library

#Defined private variables, so only student can access Student's class variables

class Student:

    def printBookList(self,__lib):
        __lib.printBookList()

    def requestBook(self,__lib):
        __bookName=input("Request a book name to avail:")
        try:
            __lib.borrowBook(__bookName)
        except ValueError:
            print("The book you are looking for not available, please enter the book that are availble[see below for reference]")
            self.printBookList(__lib)
            self.requestBook(__lib)

    def returnBook(self,__lib):
        __bookName=input("Enter the name of a book you are returning:")
        checkInOriginalBookList=__lib.checkInOriginalBookList(__bookName)
        if checkInOriginalBookList=="Original":
            __lib.addBorrowedBook(__bookName)
        elif checkInOriginalBookList=="Duplicate":
            print("The book you are returnig does not below to this system, Please check with administrator")
            print("Book return, failed!!!")





