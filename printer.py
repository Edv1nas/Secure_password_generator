class Password_printer:
    def __init__(self, password: str) -> None:
        self.password = password

class File(Password_printer):
    def __init__(self, path: str, password: str) -> None:
        super().__init__(password)
        self.path = path
        
    #function to write data to file
    def print_to_file(self):
        f = open(self.path, "a")
        f.write(f"{self.password}\n")
        f.close()

class Console(Password_printer):
    def __init__(self, password: str) -> None:
        super().__init__(password)

    #function to print to console
    def print_to_console(self):
        print(self.password)