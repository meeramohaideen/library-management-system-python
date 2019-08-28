from Library import Library
from Student import Student
from Login import Login
def main():

    print("""
    Please login to continue,
    ---> If you are a Library staff please login, with your login credential.
    ---> If you are a student use 'student' as username and 'default' as password
    """
    )
    log = Login()
    log.getUserName()
    log.getPassword()
    check = log.validateUser()
    lib = Library(["A Song of Ice and Fire", "Justice League", "Injustice", "Injustice"])
    stu=Student()


    while True:

        if check=="LibraryAdmin":
            print(""" ==============================LIBRARY MENU==========================================
                                      1. Display all available books
                                      2. Add books 
                                      3. Dismiss/Remove a book                                                                           
                                      4. Exit()
                                      5.Log out

                      """)
            try:
                option = int(input())
            except ValueError:
                print("Please enter he option correctly,[Only numbers are allowed]")
                continue
            if option == 1:
                lib.printBookList()
            elif option == 2:
                lib.getBookNametoAdd()
            elif option==3:
                lib.getBookNametoRemove()
            elif option==4:
                break
            elif option == 5:
                main()

        elif check=='Student':
            print(""" ==============================LIBRARY MENU==========================================
                                      1. Display all available books
                                      2. Request book
                                      3. Return book                                                                         
                                      4. Exit()
                                      5.Log out

                      """)
            try:
                option = int(input())
            except ValueError:
                print("Please enter he option correctly,[Only numbers are allowed]")
                continue


            if option == 2:
                stu.requestBook(lib)
            elif option == 1:
                stu.printBookList(lib)
            elif option == 3:
                stu.returnBook(lib)
            elif option==4:
                break
            elif option==5:
                main()

        elif check==False:
            #print("Login Failed!!!")
            runAgain=input("to login again press y , to exit press n:").lower()
            if runAgain=='y':
                main()
            elif runAgain=='n':
                break
            else:
                print("Wrong Choice")
                continue


main()
