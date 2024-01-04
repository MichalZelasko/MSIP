import pylcs
from project import Configuration
from coordinates import CoordinatesRequest
from data import MetadataRequest
from handler import FileHandler
from parser import Parser
from points import PointDrawer
from unbuild import UnbuildSet
from test import test
from utils import zip_arrays, do_rescale_x, do_rescale_y

class Application:
    def __init__(self, precise = False, language = "pl", conf = Configuration()):
        self.conf             = conf
        self.input            = ""
        self.old_input_list   = []
        self.output           = ""
        self.old_output_list  = []
        self.old_service_name = ""
        self.precise          = precise
        self.prompts          = zip_arrays(self.conf.prompts_en, self.conf.prompts_pl)
        self.language         = int(language == "pl")
        self.best_idx         = -1
        self.best_lcs         = -1 
        self.service_name     = ""
        self.service_index    = -1
        self.completed        = False
        self.handle_methods   = [
            self.handle_coordinates,
            self.handle_data,
            self.handle_handler,
            self.handle_parser,
            self.handle_points,
            self.handle_unbuild,
            self.handle_test,
            self.handle_list,
            self.handle_help,
            self.handle_info,
            self.handle_exit,
            self.handle_language_change,
            self.handle_prompt_change,
            self.handle_history
        ]

    def update_lcs_info(self, name, idx):
        lcs = pylcs.lcs_sequence_length(self.service_name, name)
        if lcs > self.best_lcs:
            self.best_lcs = lcs
            self.best_idx = idx

    def recognise_service(self):
        for i, service_names in enumerate(self.conf.service_names):
            for name in service_names:
                if name == self.service_name: 
                    return i
                else:
                    self.update_lcs_info(name, i)
        if not self.precise and self.best_lcs > 2:
            return self.best_idx 
        else:
            print(self.prompts[1][self.language])   
        return -1 

    def run_handler(self, service_number):
        handler = self.handle_methods[service_number] 
        handler()

    def handle_input(self, message):
        if not self.completed:
            print(message)
            self.old_input_list.append(self.input)
            self.input = input(self.conf.prompt)
            if self.input in self.conf.service_names[10]: 
                self.handle_exit()

    def handle_error(self):  
        print(self.prompts[2][self.language])

    def handle_coordinates(self):        
        self.handle_input(self.prompts[3][self.language])
        sector = self.input
        self.handle_input(self.prompts[4][self.language])
        index  = self.input
        if not self.completed:
            try:
                request = CoordinatesRequest(sector, index)
                x, y    = request.get_coordinates()
                print(f"x = {x}, y = {y}")
            except:
                self.handle_error()

    def handle_data(self):
        self.handle_input(self.prompts[5][self.language])
        self.handle_input(self.prompts[6][self.language])
        if not self.completed:
            try:
                x = float(self.old_input_list[-1])
                x = do_rescale_x(x)
                y = float(self.input)
                y = do_rescale_y(y)
                if x is None or y is None:
                    self.handle_error()
                else:
                    request = MetadataRequest(x, y, conf = self.conf)
                    print(request.get_metadata())
            except:
                self.handle_error()

    def handle_handler(self):
        self.handle_input(self.prompts[7][self.language])
        filename   = self.input        
        if not self.completed:
            try:
                reader = FileHandler(filename, conf = self.conf)
                reader.process()
            except:
                self.handle_error()

    def handle_parser(self):
        try:
            parser = Parser()
            parser.parse()
        except:
            self.handle_error()

    def handle_points(self):
        self.handle_input(self.prompts[8][self.language])
        self.handle_input(self.prompts[9][self.language])     
        if not self.completed:
            try:
                number   = int(self.old_input_list[-1])
                filename = self.input   
                drawer   = PointDrawer(number, filename, conf = self.conf)
                drawer.write()
            except:
                self.handle_error()

    def handle_unbuild(self):
        self.handle_input(self.prompts[10][self.language])
        filename   = self.input        
        if not self.completed:
            try:
                unbuild_set = UnbuildSet(filename, conf = self.conf)
                _           = unbuild_set.get_unbuild_set()
                print(unbuild_set)
            except:
                self.handle_error()

    def handle_test(self):
        test()

    def handle_list(self):
        for service in self.conf.service_list:
            print(service)

    def handle_help(self):
        if self.language: 
            description = self.conf.service_description_pl
        else:
            description = self.conf.service_description_en
        for i, service in enumerate(self.conf.service_list):
            print(service.ljust(16), "->", description[i])

    def handle_info(self):
        if self.language:
            print(self.conf.info_pl)
        else:
            print(self.conf.info_en)

    def handle_exit(self):
        self.completed = True

    def handle_language_change(self):
        self.language = 1 - self.language
        print(self.prompts[11][self.language])

    def handle_prompt_change(self):
        self.handle_input(self.prompts[12][self.language])
        if not self.completed:
            self.conf.change_prompt(self.input[0])
            print(self.prompts[13][self.language])
        
    def handle_history(self):
        print(f"{(str(0) + self.conf.dot).ljust(5)} {self.input}")
        for i, command in enumerate(reversed(self.old_input_list[1:])):
            print(f"{(str(i + 1) + self.conf.dot).ljust(5)} {command}")

    def run(self):
        while not self.completed:
            self.handle_input(self.prompts[0][self.language])
            self.service_name  = self.input
            self.service_index = self.recognise_service()
            self.run_handler(self.service_index)