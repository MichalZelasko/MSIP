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
            f"Proszę wprowadzić współrzędną X: \nLiczba pomiedzy {round(self.min_x, 2)} i {round(self.max_x, 2)} (rzeczywisty zakres) \nlub liczbę pomiędzy {0.0} i {self.scale} (zostanie przeskalowane na zakres rzeczywisty)",
            f"Proszę wprowadzić współrzędną Y: \nLiczba pomiędzy {round(self.min_y, 2)} i {round(self.max_y, 2)} (rzeczywisty zakres) \nlub liczbę pomiędzy {0.0} i {self.scale} (zostanie przeskalowane na zakres rzeczywisty)",
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
        
        self.help_en                = f" \
The application allows you to execute the following commands (each command and argument are transferred to the application upon confirmation by pressing the Enter button): \n \
\n \
coordinates     -> Finds the coordinates of a plot based on its data: \n \
                        -> Requires entering the registration area designation and precinct number [e.g. S-23], \n \
                        -> Requires entering the registration plot number. \n \
data            -> Finds information about a plot based on its coordinates \n \
                        -> Requires input of the X coordinate: \n \
                        A number between {self.min_x} and {self.max_x} (actual range) \n \
                        or a number between {0.0} and {self.scale} (will be scaled to actual range), \n \
                        -> Requires entering the Y coordinate: \n \
                        A number between {self.min_y} and {self.max_y} (actual range) \n \
                        or a number between {0.0} and {self.scale} (will be scaled to actual range). \n \
handler         -> Finds information about all plots from the specified file \n \
                        -> Requires entering the file name with indexes of cadastral plots (file location \"{self.input_directory}/[filename]\"). \n \
parser          -> Converts a .txt file to a .csv file. \n \
points          -> Randomize the indicated number of points and find data for the plots related to these points: \n \
                        -> Requires entering the number of points to be drawn. \n \
unbuild         -> Lists all unbuilt plots: \n \
                        -> Requires entering the name of the file in which the information is to be saved (the file will be saved in \"{self.output_directory}[filename]\"). \n \
test            -> Tests the application. \n \
list            -> Lists all available services. \n \
help            -> Displays help. \n \
info            -> Displays information about the application. \n \
exit            -> Exit the application - can be entered in any designated place. \n \
language        -> Changes the language [en -> pl]. \n \
prompt          -> Changes the prompt symbol. \n \
history         -> Displays a list of passed arguments (entered commands and arguments). \n"
        
        self.help_pl                = f" \
Aplikacja umozliwia wykonywanie następujących komend (każda komenda i argument zostają przekazane do aplikacji w momencie zatwierdzenia poprzez wciśnięcie przycisku Enter): \n \
 \n \
coordinates     -> Znajduje współrzędne działki w oparciu o jej dane: \n \
                        -> Wamaga wprowadzenia oznaczenia obszaru ewidencyjnego i numer obrębu [np. S-23], \n \
                        -> Wymaga wprowadzenia numeru działki ewidencyjnej. \n \
data            -> Znajduje informacje o działce w oparciu o jej współrzędne \n \
                        -> Wymaga wprowadzenia współrzędnej X:  \n \
                        Liczba pomiedzy {self.min_x} i {self.max_x} (rzeczywisty zakres) \n \
                        lub liczbę pomiędzy {0.0} i {self.scale} (zostanie przeskalowane na zakres rzeczywisty), \n \
                        -> Wymaga wprowadzenia współrzędnej Y:  \n \
                        Liczba pomiedzy {self.min_y} i {self.max_y} (rzeczywisty zakres) lub \n \
                        liczbę pomiędzy {0.0} i {self.scale} (zostanie przeskalowane na zakres rzeczywisty). \n \
handler         -> Znajduje informacje o wszystkich działkach ze wskazanego pliku \n \
                        -> Wymaga wprowadzenia nazwy pliku z indeksami działek ewidencyjnych (lokalizacja pliku \"{self.input_directory}[filename]\"). \n \
parser          -> Zamienia plik .txt na plik .csv. \n \
points          -> Wylosuj wskazaną liczbę punktów i znajdź dane dla działek związanych z tymi punktami: \n \
                        -> Wymaga wprowadzenia liczby punktów do wylosowania. \n \
unbuild         -> Wylicza wszystkie niezabudowane działki: \n \
                        -> Wymaga wprowadzenia nazwy pliku, w którym informacje mają zostać zapisane (plik zostanie zapisany w \"{self.output_directory}[filename]\"). \n \
test            -> Testuje aplikację. \n \
list            -> Wymienia wszystkie dostepne usługi. \n \
help            -> Wyświetla pomoc. \n \
info            -> Wyświetla informacje o aplikacji. \n \
exit            -> Wyjsie z aplikacji - można wpisać w każdym do tego przenaczonym miejscu. \n \
language        -> Zmienia język [pl -> en]. \n \
prompt          -> Zmienia symbol podpowiedzi. \n \
history         -> Wyświetla listę przekazanych argumentów (wpisanych poleceń i arguemntów)."
        
    def change_prompt(self, symbol):
        self.prompt = symbol