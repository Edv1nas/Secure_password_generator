import string
import secrets
import printer as pt
import logging


logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Password_Generator:

    def __init__(self, password_symbols: str, password_lenght: int) -> None:
        if password_lenght < 1:
            raise ValueError("Password length can't be zero.") 
        self.password_symbols = password_symbols # will hold the characters from which it will generate password
        self.password_lenght = password_lenght # lenght of password
        self.password = "" # Empty

    #function to get generated password
    def generate_password(self): 
        for lenght  in range(self.password_lenght):
            self.password += "".join(secrets.choice(self.password_symbols))
        logging.info("Simple password generated: %s", self.password)
        return self.password

    #function to get generated password    
    def get_password(self): 
        return self.password

#generates weak password with only letters
class Password_With_Only_Letters(Password_Generator):
    def __init__(self, lenght: int = 8) -> None:
        super().__init__(string.ascii_letters, lenght)

#generates avarage password with letters and digits
class Password_With_Letters_And_Digits(Password_Generator):
    def __init__(self, lenght: int = 10) -> None:
        super().__init__(string.ascii_letters + string.digits, lenght)

#generates strong password with letters, digits and special symbols
class Password_With_All_Symbols(Password_Generator):
    def __init__(self, lenght: int = 12) -> None:
        super().__init__(string.ascii_letters + string.digits + string.punctuation, lenght)

    #overriding, taking function from Password_Generator class
    def generate_password(self):
        super().generate_password()
        self.password += "."


while True:
    print("------------------------------------------------------")
    print("SECURE PASSWORD GENERATOR")
    print("1. Password only with letters")
    print("2. Password with letters and digits")
    print("3. Password with letters, digits and special symbols")
    print("4. Exit program")
    print("------------------------------------------------------")

    try:
        choice = int(input("Enter your choice: "))
        if choice > 4 or choice == 0:
            raise ValueError("Invalid choice")
    except ValueError:
        print("Invalid input for menu choice.")#logging.error
        continue

    if choice == 4:
        print("Thank you for using password generator!")
        break

    try:
        inputed_length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input for password length.")#logging.error
        continue
    
    password = None
    
    if choice == 1:
        password = Password_With_Only_Letters(inputed_length)
    elif choice == 2:
        password = Password_With_Letters_And_Digits(inputed_length)
    elif choice == 3:
        password = Password_With_All_Symbols(inputed_length)

    password.generate_password()

    pt.Console(f"Generated password: {password.get_password()}").print_to_console()
    pt.File("password.txt",password.get_password()).print_to_file()