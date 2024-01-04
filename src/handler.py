import csv
import numpy as np
import pandas as pd
from coordinates import CoordinatesRequest
from data import MetadataRequest
from project import Configuration

class FileHandler:
    def __init__(self, filename: str, conf = Configuration()):
        self.conf           = conf
        self.filename       = filename
        self.filepath       = self.conf.input_directory + filename
        self.headers        = []
        self.current_header = []
        self.records        = []
        self.coord_request  = None
        self.data_request   = None
        self.error          = False

    def headers_append(self, record: str):
        for item in record:
            if item not in self.headers:
                self.headers.append(item)
                self.current_header.append(item)

    def record_to_dict(self, record: str):
        record_dict = dict()
        for i, item in enumerate(record):
            record_dict[self.current_header[i]] = item
        return record_dict
    
    def parse_id(self, quater_id: str, id: str):
        quater_class = self.conf.quater_dictionary[quater_id]
        sector_id    = int(id[9:13])
        number_id    = id.split(".")[2]
        sector       = quater_class + "-" + str(sector_id)
        return sector, number_id
    
    def initialize_coord_request(self, sector: str, number_id: int | str):
        if self.coord_request is None: 
            self.coord_request = CoordinatesRequest(sector, number_id)
        else:
            self.coord_request.reset(sector, number_id)

    def perform_coord_request(self, sector: str, number_id: int | str):
        self.initialize_coord_request(sector, number_id)
        x, y = self.coord_request.get_coordinates()
        return x, y
    
    def retry_coord_request(self, number: int):
        x, y = self.coord_request.retry(number)
        return x, y

    def initialize_data_request(self, x: float, y: float):
        if self.data_request is None: 
            self.data_request = MetadataRequest(x, y)
        else:
            self.data_request.reset(x, y)

    def perform_data_request(self, x: float, y: float):
        self.initialize_data_request(x, y)
        request_dict = self.data_request.get_metadata()
        return request_dict
    
    def perform_requests(self, sector: str, number_id: int):
        x, y         = self.perform_coord_request(sector, number_id)
        request_dict = self.perform_data_request(x, y)
        return request_dict
    
    def join_record_request(self, record_dict: dict, request_dict: dict):
        if self.validate_request(record_dict, request_dict):
            for key, value in request_dict.items():
                record_dict[key] = value
                if key not in self.headers:
                    self.headers.append(key)
            self.error = False
        else:
            self.error = True
            print(f"Incorrect polygon identifier! {record_dict['DZ_IDENT']}, {request_dict['dzk_ident']}")
        return record_dict
    
    def validate_request(self, record_dict: dict, request_dict: dict):
        return 'dzk_ident' not in request_dict.keys() \
        or request_dict['dzk_ident'] == record_dict['DZ_IDENT']    

    def retry(self, number: int, record_dict: dict):
        x, y         = self.retry_coord_request(number)
        request_dict = self.perform_data_request(x, y)
        record_dict  = self.join_record_request(record_dict, request_dict) 
        return record_dict

    def retry_request(self, record_dict: dict):
        number            = 0
        while self.error and number < self.conf.max_retries:
            record_dict   = self.retry(number, record_dict)
            number        = number + 1
        return record_dict

    def record_parse(self, record):
        record_dict       = self.record_to_dict(record)
        quater_id         = record_dict['TERYT']
        id                = record_dict['DZ_IDENT']
        sector, number_id = self.parse_id(quater_id, id)
        request_dict      = self.perform_requests(sector, number_id)
        record_dict       = self.join_record_request(record_dict, request_dict)
        record_dict       = self.retry_request(record_dict)        
        self.records.append(record_dict)      

    def read(self):
        with open(self.filepath, mode='r', encoding=self.conf.encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=self.conf.delimiter)
            for i, record in enumerate(reader):
                if i == 0: self.headers_append(record)
                else     : self.record_parse(record)  

    def get_parsed_records(self):
        self.read()
        return self.headers, self.records  

    def parse_value(self, value):
        value = str(value).replace("&oacute;", "ó")
        value = value.replace("&Oacute;", "Ó")
        value = value.replace(";", "")
        value = value.replace(",", " ")
        return value  

    def process_record(self, record: dict):
        record_processed = []
        for key in self.headers:
            try   : value = self.parse_value(record[key])
            except: value = None
            record_processed.append(value)
        return record_processed
    
    def process_record_short(self, record: dict):
        record_processed = []
        for key in self.conf.columns:
            try   : value = self.parse_value(record[key])
            except: value = None
            record_processed.append(value)
        return record_processed

    def get_dataframe(self):
        _, _             = self.get_parsed_records()
        self.raw_records = []
        for record in self.records:
            processed_record = self.process_record(record)   
            self.raw_records.append(processed_record)

    def get_short_dataframe(self):
        _, _               = self.get_parsed_records()
        self.short_records = []
        for record in self.records:
            processed_record = self.process_record_short(record)   
            self.short_records.append(processed_record)

    def write(self, option = False):
        if not option: 
            records  = self.raw_records
            headers  = self.headers
            addition = self.conf.long
        else     : 
            records  = self.short_records
            headers  = self.conf.columns
            addition = self.conf.short        
        with open(self.conf.output_directory + self.filename[:-4] + addition + '.csv', 'w') as f:
            writer = csv.writer(f, delimiter=self.conf.delimiter)            
            writer.writerow(headers)
            for record in records:
                writer.writerow(record)

    def process_long(self):        
        self.get_dataframe()
        self.write(False)

    def process_short(self):
        self.get_short_dataframe()
        self.write(True)

    def process(self, short = False):
        if short: self.process_short()
        else    : self.process_long()

if __name__ == "__main__":
    reader = FileHandler('niezabudowane.csv')
    reader.process()