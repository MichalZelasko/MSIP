from coordinates import CoordinatesRequest
from data import MetadataRequest
from handler import FileHandler
from parser import Parser
from points import PointDrawer
from project import Configuration
from unbuild import UnbuildSet

conf = Configuration()

def test_coordinates():
    request = CoordinatesRequest("S-23", 19)
    x, y    = request.get_coordinates()
    print(f"x = {x}, y = {y}")

def test_data():
    request = MetadataRequest(7416228.305192139, 5545693.360041712)
    print(request.get_metadata())

def test_handler():
    reader = FileHandler('niezabudowane.csv')
    reader.process()

def test_parser():
    parser = Parser()
    parser.parse()

def test_points():
    drawer = PointDrawer(10, "points.csv")
    drawer.write()

def test_unbuild():
    unbuild_set = UnbuildSet()
    print(unbuild_set)
    _           = unbuild_set.get_unbuild_set()
    print(unbuild_set)

def test():
    test_coordinates()
    test_data()
    test_parser()
    test_points()
    test_unbuild()

if __name__ == "__main__":
    test()