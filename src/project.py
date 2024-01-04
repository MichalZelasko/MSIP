class Configuration:
    def __init__(self):
        self.max_retries            = 16
        self.tolerance              = 0.1        
        self.max_x                  = 7443881.843806132
        self.min_x                  = 7413470.395531283
        self.max_y                  = 5555025.620911894
        self.min_y                  = 5537348.98572565
        self.parse_length           = -1
        self.scale                  = 100.0

        self.prompt                 = ">"
        self.dot                    = "."
        self.delimiter              = ";"
        self.encoding               = "utf-8"
        self.input_directory        = "../files/input/"
        self.output_directory       = "../files/output/"
        self.parsed_directory       = "../files/parsed/"
        self.long                   = "_long"
        self.short                  = "_short"

        self.quater_dictionary      = {
            "126102_9": "K",
            "126103_9": "NH",
            "126104_9": "P",
            "126105_9": "S",
        }
        self.reverse_dictionary     = {
            "K" : "126102_9",
            "NH": "126103_9",
            "P" : "126104_9",
            "S" : "126105_9",
        }
        self.quater_names           = {
            "K-": "Krowodrza",
            "NH": "Nowa Huta",
            "P-": "Podgórze",
            "S-": "Śródmieście",
        }
        self.columns                = [
            "Teryt",
            "DZ_IDENT",
            "GR_WL_OP",
            "opis_oznac"
        ]
        self.header_list            = [
            "je_nr",
            "obr_nazwa",
            "nr",
            "id",
            "opis_oznac"
        ]
        self.service_list           = [
            "coordinates",
            "data",
            "handler",
            "parser",
            "points",
            "unbuild",
            "test",
            "list",
            "help",
            "info",
            "exit",
            "language",
            "prompt",
            "history"
        ]
        self.service_description_pl = [
            "Znajdź współrzędne działki w oparciu o jej dane",
            "Znajdź informacje o działce w oparciu o jej współrzędne",
            "Znajdź informacje o wszystkich działkach ze wskazanego pliku",
            "Zamień plik .txt na plik .csv",
            "Wylosuj wskazaną liczbę punktów i znajdź dane dla działek związanych z tymi punktami",
            "Wylicz wszystkie niezabudowane działki",
            "Przetestuj aplikację",
            "Wymień wszystkie dostepne usługi",
            "Pomóż",
            "Informacje o aplikacji",
            "Wyjdź",
            "Zmiana języka [pl -> en]",
            "Zmiana symbolu podpowiedzi",
            "Lista przekazanych argumentów"
        ]
        self.service_description_en = [
            "Find coordinates of given polygon.",
            "Find data for polygon with given coordinates",
            "Find data for all polygons mentioned in given file",
            "Parse given .txt file to .csv",
            "Draw given number of points and find polygon data referring to those points",
            "Enumerate all unbuild polygons",
            "Test the application",
            "List all services",
            "Help",
            "App information",
            "Exit",
            "Language change [en -> pl]",
            "Prompt symbol change",
            "List of given arguments"
        ]
        self.service_names          = [
            ["coordinates", "coord", "c", "Find coordinates of given polygon.", "Znajdź współrzędne działki w oparciu o jej dane"],
            ["data", "d", "Find data for polygon with given coordinates", "Znajdź informacje o działce w oparciu o jej współrzędne"],
            ["handler", "handle", "Find data for all polygons mentioned in given file", "Znajdź informacje o wszystkich działkach ze wskazanego pliku", "Wczytaj dane punktów z pliku"],
            ["parser", "parse", "Parse given .txt file to .csv", "Zamień plik .txt na plik .csv"],
            ["points", "point", "p", "Draw given number of points and find polygon data referring to those points", "Wylosuj wskazaną liczbę punktów i znajdź dane dla działek związanych z tymi punktami"],
            ["unbuild", "un", "u", "Enumerate all unbuild polygons", "Wylicz wszystkie niezabudowane działki"],
            ["test", "t", "Test the application", "Przetestuj aplikację"],
            ["list", "l", "List all services", "Wymień wszystkie dostepne usługi"],
            ["help", "h", "Help", "Pomóż"],
            ["info", "i", "inf", "App information", "Informacje o aplikacji"],
            ["exit", "e", "wyjdź", "opuść", "w"],
            ["language", "lan", "lang", "Language change", "Zmiana języka"],
            ["prompt", "prom", "Prompt symbol change", "Zmiana symbolu podpowiedzi"],
            ["history", "hist", "historia", "his"]
        ]
        self.prompts_pl             = [
            "Wprowadź nazwę serwisu, z którego chcesz skorzystać:",
            "UWAGA: Nie rozpoznano usługi! Możesz ustawić opcję \"precise\" na False aby umożliwić nieprecyzyjne dopasowywanie do wzorca",
            "Błąd podczas wykonywania polecenia\nCzy wprowadziłeś/-aś poprawne argumenty wykonania",
            "Proszę wprowadź oznaczenia obszaru ewidencyjnego i numer obrębu [np. S-23]:",
            "Proszę wprowadzić numer działki ewidencyjnej:",
            f"Proszę wprowadzić współrzędną X: \nLiczba pomiedzy {round(self.min_x, 2)} i {round(self.max_x, 2)} (rzeczywisty zakres) \nlub liczbę pomiędzy {0.0} i {100.0} (zostanie przeskalowane na zakres rzeczywisty)",
            f"Proszę wprowadzić współrzędną Y: \nLiczba pomiędzy {round(self.min_y, 2)} i {round(self.max_y, 2)} (rzeczywisty zakres) \nlub liczbę pomiędzy {0.0} i {100.0} (zostanie przeskalowane na zakres rzeczywisty)",
            f"Proszę wprowadzic nazwę pliku z indeksami działek ewidencyjnych (lokalizacja pliku {self.input_directory}[filename]):",
            f"Proszę wprowadzic liczbę punktów do wylosowania:",
            f"Proszę wprowadzić nazwę pliku, w którym informacje mają zostac zapisane (plik zostanie zapisany w {self.output_directory}[filename]):",
            f"Proszę wprowadzić nazwę pliku, w którym znajdują sie indeksy działek niezabudowanych (lokalizacja pliku {self.input_directory}[filename]):",
            "Język został zmieniony na język polski.",
            "Proszę wprowadzić nowe oznaczenie symbolu podpowiedzi.",
            f"Nowy symbol podpowiedzi to {self.prompt}"
        ]
        self.prompts_en             = [
            "Please enter service name:",
            "WARNING: Service cannot be recognised! You can set \"precise\" option as False to enable pattern matching",
            "ERROR while running given command!\nDid you entered correct arguments?",
            "Please enter the registration area designations and precinct number [e.g. S-23]:",
            "Please enter the registration plot number:",
            f"Please enter X coordinate: \nNumber between {round(self.min_x, 2)} and {round(self.max_x, 2)} (real range)\nor number between {0.0} and {self.scale} (it will be scaled to above range)",
            f"Please enter Y coordinate:\nNumber between {round(self.min_y, 2)} and {round(self.max_y, 2)} (real range)\nor number between {0.0} and {self.scale} (it will be scaled to above range)",
            f"Please enter name of the file with plots identifiers (file location: {self.input_directory}[filename]):",
            f"Please enter number of points to draw:",
            f"Please enter destination file name (file will be saved in {self.output_directory}[filename]):",
            f"Please enter name of file containing data of unbuild plots identifiers (file location {self.input_directory}[filename]):",
            "Language was change, now it's English.",
            "Please enter new prompt symbol.",
            f"New prompt symbol is {self.prompt}"
        ]
        self.info_pl                = "Aplikacja REST do obsługi serwisu MSIP.\n@Prawa autorskie: Michał Żelasko\n \
Żródło: https://github.com/MichalZelasko/MSIP\n \
Kontakt: zelaskomj@gmail.com, Messenger\n \
Opis: Aplikacja może byc wykorzystana do ściaganie informacji z https://msip.um.krakow.pl/kompozycje/ przy użyciu zapytań REST, \n \
przetwarzania zebranych danych i tworzenia plików wyjsciowych zawierających wszystkie informacje odnoszące się do wskazanego obszaru. \n \
Głównym celem projektu jest umożliwienie dostępu do serwisu MSIP dla studentów studiów magisterskich \n \
realizujących prace magisterskie wymagające dostępu danych przestrzennych."
        self.info_en                = f"REST application for MSIP system.\n \
@Copyrights: Michał Żelasko\n \
Source: https://github.com/MichalZelasko/MSIP\n \
Contact: zelaskomj@gmail.com, Messenger\n \
Description: Application can be used to download data from https://msip.um.krakow.pl/kompozycje/ with REST request, \n \
parse gathered data and produce output files containing all information regarding particular polygons. \n \
Main objective of the project is to enable access to MSIP web service for master degree students realizing master degrees \n \
requiring access to above mentioned polygon data."
        
    def change_prompt(self, symbol):
        self.prompt = symbol