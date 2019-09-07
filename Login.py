"""
Defined sample user name and password for library admin, and check for the credentials
Student can login with default credentials
"""

class Login:
    def __init__(self):
        self.UserDetailsLibraryAdmin = {
            'admin01': 'Password01',
            'admin02': 'Password02',
            'admin03': 'Password03'
        }
        self.UserDetailsStudent = {
            'student': 'default'
        }

    def getUserName(self):
        self.userName = input("Enter User name:")

    def getPassword(self):
        self.userPassword = input("Enter User name:")

    def validateUser(self):
        try:
            if self.UserDetailsLibraryAdmin[self.userName] == self.userPassword:
                return "LibraryAdmin"
        except KeyError:
            try:
                if self.UserDetailsStudent[self.userName] == self.userPassword:
                    return "Student"
            except KeyError:
                print("Login Failed")
                return False




