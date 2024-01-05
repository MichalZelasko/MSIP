# MSIP

## [Polski]

## REST application to handle access to MSIP system.

### Instalacja

Aby pobrać: "Code" - nad listą plików i katalogów po prawej stronie i -> "Download Zip". Następnie zapisany na komputerze plik należy rozpakować (Windows: prawy przycisk myszy -> Wyodrębnij wsszystkie, Linux: "sudo apt-get install unzip" i "unzip archive.zip") i przejść do nadrzędnego katalogu projektu.

Przed uruchomieniem aplikacji należy upewnić się, że na komputerze zainstalowany jest Python (wersja zalecane 3.10.12) - test za pomoca komendy (dostęp do wiersza poleceń na Windowsie w Przegladarce Plików: Plik -> Otwórz program Windows Powershell (najechać i po prawej) -> Otwórz program Windows Powershell jako Administartor):

    python --version

Następnie należy upewnic się, że działa domyślny system zarządzania pakietami "pip" - można przetestować za pomocą komendy: python -m pip help. Jeśli wymaganie nie jest spełnione należy (w wierszu poleceń) wykonać komendę: 

    python get-pip.py

W kolejnym kroku należy uruchomić wierz poleceń z poziomu głównego katalogu projektu i wykonać polecenie: 

    pip install -r requirements.txt 

W kolejnym kroku należy przejść do podkatalogu /src i wykonać polecenie 

    python main.py

UWAGA: w niektórych systemach operacyjnych wymagane jest zastosowanie polecenia python3 zamiast python.


### Użytkowanie:

Aplikacja umozliwia wykonywanie następujących komend (każda komenda i argument zostają przekazane do aplikacji w momencie zatwierdzenia poprzez wciśnięcie przycisku Enter):

&NewLine;
&NewLine;

* coordinates      -> Znajduje współrzędne działki w oparciu o jej dane:

    * -> Wamaga wprowadzenia oznaczenia obszaru ewidencyjnego i numer obrębu [np. S-23],

    * -> Wymaga wprowadzenia numeru działki ewidencyjnej.

&NewLine;
&NewLine;

* data             -> Znajduje informacje o działce w oparciu o jej współrzędne

    * -> Wymaga wprowadzenia współrzędnej X: Liczba pomiedzy 7413470.40 i 7443881.84 (rzeczywisty zakres) lub liczbę pomiędzy {0.0} i {100.0} (zostanie przeskalowane na zakres rzeczywisty),

    * -> Wymaga wprowadzenia współrzędnej Y: Liczba pomiedzy 5537348.99 i 5555025.62 (rzeczywisty zakres) lub liczbę pomiędzy {0.0} i {100.0} (zostanie przeskalowane na zakres rzeczywisty).

&NewLine;
&NewLine;

* handler          -> Znajduje informacje o wszystkich działkach ze wskazanego pliku

    * -> Wymaga wprowadzenia nazwy pliku z indeksami działek ewidencyjnych (lokalizacja pliku "../files/input/[filename]").

&NewLine;
&NewLine;

* parser           -> Zamienia plik .txt na plik .csv.

&NewLine;
&NewLine;

* points           -> Wylosuj wskazaną liczbę punktów i znajdź dane dla działek związanych z tymi punktami:

    * -> Wymaga wprowadzenia liczby punktów do wylosowania.

&NewLine;
&NewLine;

* unbuild          -> Wylicza wszystkie niezabudowane działki:

    * -> Wymaga wprowadzenia nazwy pliku, w którym informacje mają zostać zapisane (plik zostanie zapisany w "../files/output/[filename]").

&NewLine;
&NewLine;

* test             -> Testuje aplikację.

&NewLine;
&NewLine;

* list             -> Wymienia wszystkie dostepne usługi.

&NewLine;
&NewLine;

* help             -> Wyświetla pomoc.

&NewLine;
&NewLine;

* info             -> Wyświetla informacje o aplikacji.

&NewLine;
&NewLine;

* exit             -> Wyjsie z aplikacji - można wpisać w każdym do tego przenaczonym miejscu.

&NewLine;
&NewLine;

* language         -> Zmienia język [pl -> en].

&NewLine;
&NewLine;

* prompt           -> Zmienia symbol podpowiedzi.

&NewLine;
&NewLine;

* history          -> Wyświetla listę przekazanych argumentów (wpisanych poleceń i arguemntów).


## [English]

## REST application for handling access to the MSIP system.

### Installation

To download: "Code" - above the list of files and directories on the right and -> "Download Zip". Then, unpack the file saved on your computer (Windows: right mouse button -> Extract all, Linux: "sudo apt-get install unzip" and "unzip archive.zip") and go to the parent project directory.

Before running the application, make sure that Python is installed on your computer (recommended version 3.10.12) - test using the command (access to the command line on Windows in the File Browser: File -> Open Windows Powershell (hover and right) -> Open Windows Powershell as Administrator):

    python --version

Then make sure that the default package management system "pip" is working - you can test it with the command: python -m pip help. If the requirement is not met, execute the command (in the command line):

    python get-pip.py

In the next step, run the command line from the main project directory and execute the command:

    pip install -r requirements.txt

In the next step, go to the /src subdirectory and execute the command

    python main.py

NOTE: Some operating systems require the python3 command instead of python.

### Usage:

The application allows you to execute the following commands (each command and argument are transferred to the application upon confirmation by pressing the Enter button):

&NewLine;
&NewLine;

* coordinates     -> Finds the coordinates of a plot based on its data:

    * -> Requires entering the registration area designation and precinct number [e.g. S-23],

    * -> Requires entering the registration plot number.

&NewLine;
&NewLine;

* data            -> Finds information about a plot based on its coordinates

    * -> Requires input of the X coordinate. A number between 7413470.40 and 7443881.84 (actual range) or a number between {0.0} and {100.0} (will be scaled to actual range),

    * -> Requires entering the Y coordinate: A number between 5537348.99 and 5555025.62 (actual range) or a number between {0.0} and {100.0} (will be scaled to actual range).

&NewLine;
&NewLine;

* handler         -> Finds information about all plots from the specified file

    * -> Requires entering the file name with indexes of cadastral plots (file location "../files/input/[filename]").

&NewLine;
&NewLine;

* parser          -> Converts a .txt file to a .csv file.

&NewLine;
&NewLine;

* points          -> Randomize the indicated number of points and find data for the plots related to these points:

    * -> Requires entering the number of points to be drawn.

&NewLine;
&NewLine;

* unbuild         -> Lists all unbuilt plots:

    * -> Requires entering the name of the file in which the information is to be saved (the file will be saved in "../files/output/[filename]").

&NewLine;
&NewLine;

* test            -> Tests the application.

&NewLine;
&NewLine;

* list            -> Lists all available services.

&NewLine;
&NewLine;

* help            -> Displays help.

&NewLine;
&NewLine;

* info            -> Displays information about the application.

&NewLine;
&NewLine;

* exit            -> Exit the application - can be entered in any designated place.

&NewLine;
&NewLine;

* language        -> Changes the language [en -> pl].

&NewLine;
&NewLine;

* prompt          -> Changes the prompt symbol.

&NewLine;
&NewLine;

* history         -> Displays a list of passed arguments (entered commands and arguments).