from project import Configuration

conf = Configuration()

class Parser:
    def __init__(self, filename = "niezabudowane.txt", n = -1, conf = Configuration()):
        self.conf     = conf
        self.filepath = self.conf.input_directory + filename
        self.filename = filename
        self.header   = ""
        self.lines    = []
        self.number   = n

    def parse(self):
        self.read()
        self.write()

    def read(self):
        self.numbers = set()
        with open(self.filepath, mode='r', encoding=self.conf.encoding) as file:
            lines = file.readlines()
            for i, record in enumerate(lines):                
                if i != 0: 
                    self.completed = True
                    line           = record.replace(" ", ";", 1) \
                                           .replace(" ", ";", 1)
                    self.lines.append(line)
                else:
                    self.header = record.replace(" ", ";")

    def write(self):
        self.numbers = set()
        with open(self.conf.parsed_directory + self.filename[:-4] + ".csv", mode='w') as file:
            file.write(self.header)
            for line in self.lines[:self.conf.parse_length]:
                file.write(line)

if __name__ == "__main__":
    parser = Parser()
    parser.parse()