import requests
import numpy as np
import warnings
from project import Configuration

class MetadataRequest:
    def __init__(self, x: float, y: float, conf = Configuration()):
        self.conf = conf
        self.reset(x, y)

    def reset(self, x: float, y: float):
        self.reset_coordinates(x, y)
        self.reset_response()
        self.reset_data()
        self.reset_adress()

    def reset_response(self):
        self.error                 = False
        self.error_status          = False
        self.error_marking         = False
        self.error_place           = False
        self.response              = ""
        self.response_text         = None
        self.response_status       = ""
        self.response_status_text  = None
        self.response_marking      = ""
        self.response_marking_text = None
        self.response_place        = ""
        self.response_place_text   = None

    def reset_coordinates(self, x: float, y: float):
        self.x = x
        self.y = y

    def reset_data(self):
        self.keys   = []
        self.values = []

    def reset_adress(self):
        self.adress         = None 
        self.status_adress  = None 
        self.marking_adress = None    
        self.place_adress   = None 
    
    def build_code_request(self):
        self.adress = f"https://msip.um.krakow.pl//arcgis/rest/services/Obserwatorium/GI_EGIB/MapServer/1/query? \
                        f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A \
                        {self.x - self.conf.tolerance}%2C%22ymin%22%3A{self.y - self.conf.tolerance}%2C%22xmax%22%3A \
                        {self.x + self.conf.tolerance}%2C%22ymax%22%3A{self.y + self.conf.tolerance}%2C%22 \
                        spatialReference%22%3A%7B%22wkid%22%3A2178%7D%7D&geometryType=esriGeometryEnvelope \
                        &inSR=2178&outFields=ESRI_OID%2Cgeom%2Cje_nr%2Cje_nazwa%2Cobr_nazwa%2Cnr%2Cid \
                        %2Cpow_ewid%2Cpow_graf%2Caktualnosc%2Cid_iip%2Ctz%2Cdzk_ident%2Ccounter&outSR=2178"

    def build_status_request(self):
        self.status_adress = f"https://msip.um.krakow.pl//arcgis/rest/services/Obserwatorium/BP_MPZP/MapServer/dynamicLayer/query? \
                               f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A \
                               {self.x - self.conf.tolerance}%2C%22ymin%22%3A{self.y - self.conf.tolerance}%2C%22xmax%22%3A \
                               {self.x + self.conf.tolerance}%2C%22ymax%22%3A{self.y + self.conf.tolerance}%2C%22 \
                               spatialReference%22%3A%7B%22wkid%22%3A2178%7D%7D&geometryType=esriGeometryEnvelope \
                               &inSR=2178&outFields=nazwa%2Cuchwalenie%2Cdata_uchwa%2Cogloszenie%2Cdata_duwm%2Cdata_obowi \
                               %2Cwww%2Cgeom%2Cstatus%2Cprzystapie%2Cdata_przys%2Cprowadzacy%2Cwykonanie%2Cuchwala_od \
                               %2Cid_pg&outSR=2178&layer=%7B%22source%22%3A%7B%22type%22%3A%22mapLayer%22%2C%22mapLayerId%22%3A4%7D%7D"
        
    def build_marking_request(self):
        self.marking_adress = f"https://msip.um.krakow.pl//arcgis/rest/services/Obserwatorium/BP_MPZP/MapServer/dynamicLayer/query? \
                                f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22%3A \
                                {self.x - self.conf.tolerance}%2C%22ymin%22%3A{self.y - self.conf.tolerance}%2C%22xmax%22%3A \
                                {self.x + self.conf.tolerance}%2C%22ymax%22%3A{self.y + self.conf.tolerance}%2C%22 \
                                spatialReference%22%3A%7B%22wkid%22%3A2178%7D%7D&geometryType=esriGeometryEnvelope \
                                &inSR=2178&outFields=oznaczenie%2Crodzaj_ozn%2Cnazwa_mpzp%2Cdata_uchwa%2Cuchwalenie \
                                %2Cogloszenie%2Cdata_duwm%2Cdata_obowi%2Cwww%2Cgdb_id%2Copis_oznac%2Cgeom%2Cid_pg \
                                &outSR=2178&layer=%7B%22source%22%3A%7B%22type%22%3A%22mapLayer%22%2C%22mapLayerId%22%3A1%7D%7D"
        
    def build_place_request(self):
        self.place_adress = f"https://msip.um.krakow.pl//arcgis/rest/services/Obserwatorium/GI_EGIB/MapServer/0/query? \
                              f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry=%7B%22xmin%22% \
                              {self.x - self.conf.tolerance}%2C%22ymin%22%3A{self.y - self.conf.tolerance}%2C%22xmax%22%3A \
                              {self.x + self.conf.tolerance}%2C%22ymax%22%3A{self.y + self.conf.tolerance}%2C%22 \
                              spatialReference%22%3A%7B%22wkid%22%3A2178%7D%7D&geometryType=esriGeometryEnvelope \
                              &inSR=2178&outFields=adr_id%2Cgeom%2Culica%2Cadr_nr%2Ckod_kod%2Cmsc_nazwa%2Caktualnosc&outSR=2178"
        
    def request_code_data(self):
        self.build_code_request() 
        try:
            warnings.filterwarnings("ignore")
            self.response      = requests.get(self.adress, verify=False)
            self.response_text = self.response.text           
        except:
            self.error = True

    def request_status_data(self):
        self.build_status_request() 
        try:
            warnings.filterwarnings("ignore")
            self.response_status      = requests.get(self.status_adress, verify=False)
            self.response_status_text = self.response_status.text           
        except:
            self.error_status = True

    def request_marking_data(self):
        self.build_marking_request() 
        try:
            warnings.filterwarnings("ignore")
            self.response_marking      = requests.get(self.marking_adress, verify=False)
            self.response_marking_text = self.response_marking.text           
        except:
            self.error_marking = True

    def request_place_data(self):
        self.build_place_request()
        try:
            warnings.filterwarnings("ignore")
            self.response_place      = requests.get(self.place_adress, verify=False)
            self.response_place_text = self.response_place.text           
        except:
            self.error_place = True

    def do_proceed(self):
        return not (self.error or self.error_status or self.error_marking or self.error_place)
    
    def verify_key_value(self, key, value):
        return len(value) > 0 \
        and ">" not in value  \
        and "<" not in value  \
        and "#" not in value  \
        and ">" not in key    \
        and "<" not in key    \
        and "#" not in key        
    
    def append_key_value(self, key, value):
        if self.verify_key_value(key, value):
            self.keys.append(key)
            try:
                self.values.append(int(value)) 
            except:
                try   : self.values.append(float(value))
                except: self.values.append(value)
    
    def extract_data(self, text):
        for line in text.splitlines():
            if "<i>" in line:
                element_list = line[3:].split("</i>")
                key          = element_list[0][:-2]
                value        = element_list[1][1:-5]
                self.append_key_value(key, value)      

    def report_error(self, text):
        print(f"Error while requesting for polygon metadata: {text}!")

    def get_code_data(self):
        self.request_code_data()
        if self.do_proceed(): self.extract_data(self.response_text)
        else                : self.report_error("Code data")
    
    def get_status_data(self):
        self.request_status_data()
        if self.do_proceed(): self.extract_data(self.response_status_text)
        else                : self.report_error("Status data")
    
    def get_marking_data(self):
        self.request_marking_data()
        if self.do_proceed(): self.extract_data(self.response_marking_text)
        else                : self.report_error("Marking data")

    def get_place_data(self):
        self.request_place_data()
        if self.do_proceed(): self.extract_data(self.response_place_text)
        else                : self.report_error("Place data")
        
    def get_metadata(self):
        self.get_code_data()
        self.get_status_data()
        self.get_marking_data()
        self.get_place_data()
        return self.create_dictionary()
    
    def create_dictionary(self):
        return_dict = dict()
        for i, key in enumerate(self.keys):
            j            = 0
            key_modified = key
            while key_modified in return_dict.keys(): 
                j            = j   + 1
                key_modified = key + f"_{j}"
            return_dict[key_modified] = self.values[i]
        return return_dict
    
if __name__ == "__main__":
    request = MetadataRequest(7416228.305192139, 5545693.360041712)
    print(request.get_metadata())
