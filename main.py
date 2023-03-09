import string
import secrets
import logging
import printer as pt
from art import text2art


logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class PasswordGenerator:

    def __init__(self, password_symbols: str, password_length: int) -> None:
        self.password_symbols = password_symbols
        self.password_length = password_length 
        self.password = "" 

    def generate_password(self) -> str: 
        for length  in range(self.password_length):
            self.password += "".join(secrets.choice(self.password_symbols))
        return self.password
  
    def get_password(self) -> str: 
        return self.password

class WeakPassword(PasswordGenerator):
    def __init__(self, length: int) -> None:
        super().__init__(string.ascii_letters, length)

class AveragePassword(PasswordGenerator):
    def __init__(self, length: int) -> None:
        super().__init__(string.ascii_letters + string.digits, length)

class StrongPassword(PasswordGenerator):
    def __init__(self, length: int) -> None:
        super().__init__(string.ascii_letters + string.digits + string.punctuation, length)

    def generate_password(self) -> str:
        super().generate_password()
        self.password += ":)"

def get_input_choice() -> int:
    while True:
        try:
            program_name=text2art("PASSWORD GENERATOR", font="smkeyboard")
            print(program_name)
            print("------------------------------------------------------")
            print("1. Only letters")
            print("2. Letters and digits")
            print("3. Letters, digits, special symbols + smile")
            print("4. Exit program")
            print("------------------------------------------------------")

            inputed_choice = int(input("Enter a number of your choice: "))
            if inputed_choice > 4 or inputed_choice == 0:
                print("\nInvalid number entered.\n")
                continue

        except ValueError as e:
            logging.error(f"Invalid user input: {e}")
            print("\nError: invalid input for menu choice.\n")
            continue
        return inputed_choice

def get_password_length() -> int:
    while True:
        try:
            inputed_length = int(input("Enter password length: "))
            if inputed_length < 4 or inputed_length > 255:
                print("\nError: password lenght can't be less then 8 or more then 255 .\n")
                continue

        except ValueError as e:
            logging.error(f"Invalid user input: {e}")
            print("\nError: invalid input for password length.\n")
            continue
        return inputed_length

if __name__ == "__main__":
    while True:
        input_choice = get_input_choice()
        if input_choice == 4:
            print("\nThank you for using password generator!")
            break

        password_length = get_password_length()

        if input_choice == 1:
            password = WeakPassword(password_length)
        elif input_choice == 2:
            password = AveragePassword(password_length)
        else:
            password = StrongPassword(password_length)
            
        password.generate_password()
        pt.Console(f"\nGenerated password: {password.get_password()}").print_to_console()
        pt.File("trash.txt",password.get_password()).print_to_file()