import requests
import numpy as np
import warnings

class CoordinatesRequest:
    def __init__(self, sector: str, number: int | str):
        self.reset(sector, number)

    def reset(self, sector: str, number: int | str):
        self.set_request(sector, number)
        self.reset_response()
        self.reset_adress()
        self.reset_coordinates()

    def set_request(self, sector: str, number: int | str):
        self.sector = sector
        self.number = number  

    def reset_adress(self):
        self.adress = None      

    def reset_response(self):
        self.error              = False
        self.response           = ""
        self.response_json      = None
        self.response_geometry  = None

    def reset_coordinates(self):
        self.x  = None
        self.y  = None
        self.xs = np.zeros(1)
        self.ys = np.zeros(1)

    def build_coordinates_request(self):
        self.adress = f"https://msip.um.krakow.pl//arcgis/rest/services/Obserwatorium/GI_EGIB/MapServer/1/query?f=json&where=obr_nazwa%20%3D%20%27{self.sector}%27%20and%20upper(nr)%20like%20upper(%27{self.number}%27)&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=nr%2Cje_nazwa%2Cobr_nazwa%2Cpow_graf%2CESRI_OID&outSR=2178"

    def coordinates_request(self):
        self.build_coordinates_request()
        try:
            warnings.filterwarnings("ignore")
            self.response           = requests.get(self.adress, verify=False)
            self.response_json      = self.response.json()
            self.response_geometry  = self.response_json['features'][0]['geometry']['rings'][0]
        except:
            self.error = True

    def do_proceed(self):
        return not self.error
    
    def extract_coordinates(self):
        n       = len(self.response_geometry)
        self.xs = np.zeros(n)
        self.ys = np.zeros(n)
        for i, point in enumerate(self.response_geometry):
            self.xs[i] = float(point[0])
            self.ys[i] = float(point[1])
        self.x = np.mean(self.xs)
        self.y = np.mean(self.ys)

    def report_error(self):
        print("Error while requesting for geometry attributes (coordinates)!")

    def get_coordinates(self):
        self.coordinates_request()
        if self.do_proceed():
            self.extract_coordinates()
        else:
            self.report_error()
        return self.x, self.y
    
    def get_error(self):
        return self.error  

    def retry(self, retry_number: int):
        n     = len(self.xs)
        idx_1 = retry_number // n
        idx_2 = retry_number %  n + idx_1
        if idx_2 >= idx_1: idx_2 = idx_2 + 1
        idx_1 = min(n - 1, idx_1)
        idx_2 = min(n - 1, idx_2)
        x     = (self.xs[idx_1] + self.xs[idx_2]) / 2
        y     = (self.ys[idx_1] + self.ys[idx_2]) / 2
        return x, y
    
def input_coordinates():
    print("Please enter sector")
    
if __name__ == "__main__":
    request = CoordinatesRequest("S-23", 19)
    x, y    = request.get_coordinates()
    print(f"x = {x}, y = {y}")
