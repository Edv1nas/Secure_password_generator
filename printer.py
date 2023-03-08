class PasswordPrinter:
    def __init__(self, password: str) -> None:
        self.password = password

class File(PasswordPrinter):
    def __init__(self, path: str, password: str) -> None:
        super().__init__(password)
        self.path = path
        
    #function to write data to file
    def print_to_file(self):
        file = open(self.path, "a")
        file.write(f"{self.password}\n")
        file.close()

class Console(PasswordPrinter):
    def __init__(self, password: str) -> None:
        super().__init__(password)

    #function to print to console
    def print_to_console(self):
        print(self.password)