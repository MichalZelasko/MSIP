from project import Configuration

class UnbuildSet:
    def __init__(self, filename = "niezabudowane.txt", conf = Configuration()):
        self.conf      = conf
        self.filename  = self.conf.input_directory + filename
        self.completed = False
        self.numbers   = set()

    def read_unbuild_set(self):
        self.numbers = set()
        with open(self.filename, mode='r', encoding=self.conf.encoding) as file:
            lines = file.readlines()
            for i, record in enumerate(lines):
                if i != 0: 
                    self.completed = True
                    number         = record.split(" ")[1]
                    self.numbers.add(number)

    def get_unbuild_set(self):
        if not self.completed:
            self.read_unbuild_set()
        return self.numbers
    
    def __str__(self):
        result_string = ""
        if self.completed:
            for index in self.numbers:
                result_string = result_string + index + "\n"
        else:
            result_string     = "Set has not been read yet!"
        return result_string

