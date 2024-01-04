import csv
import time
from random import random, seed
from data import MetadataRequest
from project import Configuration
from unbuild import UnbuildSet

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class PointDrawer:
    def __init__(self, number: int, filename: str, seed_init = 43, conf = Configuration()):
        self.conf       = conf
        self.number     = number
        self.max_x      = self.conf.max_x
        self.min_x      = self.conf.min_x
        self.max_y      = self.conf.max_y
        self.min_y      = self.conf.min_y
        self.seed       = seed_init
        self.filename   = filename
        self.range_x    = int(self.max_x - self.min_x)
        self.range_y    = int(self.max_y - self.min_y)
        self.points     = []
        self.headers    = []
        self.records    = []
        self.start      = time.time()
        self.number_set = UnbuildSet().get_unbuild_set()
        seed(self.seed)

    def draw_points(self):
        for _ in range(self.number):
            x     = self.min_x + self.range_x * random()
            y     = self.min_y + self.range_y * random()
            self.points.append(Point(x, y))

    def request_points(self, option = False):
        self.draw_points()
        if option: self.request_points_short()
        else     : self.request_points_long()

    def update_headers(self, record: dict):
        for key in record.keys():
            if key not in self.headers:
                self.headers.append(key)

    def reconstruct_record(self, point_dict: dict):
        record = dict()
        for key in self.headers:
            try:
                record[key] = point_dict[key]
            except:
                record[key] = None
        return record
    
    def report_time(self, n, i):
        print(f"Point: {str(i).ljust(8)}| Time: {str(round(time.time() - self.start, 5)).ljust(16)}| Percent: {str(round(100 * (i + 1) / n, 5)).ljust(12)}% | Predicted time: {str(round((time.time() - self.start) * n / (i + 1), 5)).ljust(16)}")

    def request_points_short(self):
        self.headers = self.conf.header_list
        self.start   = time.time()
        n            = len(self.points)
        for i, point in enumerate(self.points):
            request    = MetadataRequest(point.x , point.y)
            point_dict = request.get_metadata()
            record     = self.reconstruct_record(point_dict)
            self.records.append(record)
            self.report_time(n , i)

    def request_points_long(self):
        self.start = time.time()
        n          = len(self.points)
        for i, point in enumerate(self.points):
            request    = MetadataRequest(point.x , point.y)
            record     = request.get_metadata()
            self.update_headers(record)
            self.records.append(record)
            self.report_time(n , i)

    def parse_value(self, value):
        value = str(value).replace("&oacute;", "ó")
        value = value.replace("&Oacute;", "Ó")
        value = value.replace(";", "")
        value = value.replace(",", " ")
        return value

    def verify_quater(self, key, record):
        value = None
        try:
            if key == 'je_nazwa':
                value = self.conf.quater_names[str(record['obr_nazwa'][:2])]
        except:
            value = None            
        return value

    def parse_records(self):
        raw_records = []
        for record in self.records:
            raw_record = []
            for key in self.headers:
                try:
                    value = self.parse_value(record[key])
                except:
                    value = self.verify_quater(key, record)
                raw_record.append(value)
            raw_records.append(raw_record)
        return raw_records
    
    def verify_unbuild(self, record):
        quater_name   = record[2].split("-")[0]
        sector_number = record[2].split("-")[1]
        number        = record[3]
        quater_index  = self.conf.reverse_dictionary[quater_name]
        identifier    = quater_index + "." + ("0" * (4 - len(sector_number))) + sector_number + "." + number
        return identifier in self.number_set
    
    def create_headers(self):
        records = self.parse_records()
        headers = self.headers
        headers.insert(0, "Niezabudowany")
        return headers, records
    
    def complete_unbuild(self, record):
        unbuild = self.verify_unbuild(record)
        record.insert(0, str(unbuild))
        return record        

    def write(self, option = False):
        self.request_points(option)
        headers, records = self.create_headers()
        with open(self.conf.output_directory + self.filename, 'w') as f:
            writer = csv.writer(f, delimiter=self.conf.delimiter)            
            writer.writerow(headers)
            for record in records:
                if len(record) != 0 and record[0] is not None:
                    record = self.complete_unbuild(record)
                    writer.writerow(record)

if __name__ == "__main__":
    drawer = PointDrawer(10, "points.csv")
    drawer.write()