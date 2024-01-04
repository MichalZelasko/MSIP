# MSIP
[Polski]

REST application to handle access to MSIP system.

Aby pobrać: "Code" - nad listą plików i katalogów po prawej stronie i -> "Download Zip". Następnie zapisany na komputerze plik należy rozpakować (Windows: prawy przycisk myszy -> Wyodrębnij wsszystkie, Linux: "sudo apt-get install unzip" i "unzip archive.zip") i przejść do nadrzędnego katalogu projektu.

Przed uruchomieniem aplikacji należy upewnić się, że na komputerze zainstalowany jest Python (wersja zalecane 3.10.12) - test za pomoca komendy (dostęp do wiersza poleceń na Windowsie w Przegladarce Plików: Plik -> Otwórz program Windows Powershell (najechać i po prawej) -> Otwórz program Windows Powershell jako Administartor):

python --version

Następnie należy upewnic się, że działa domyślny system zarządzania pakietami "pip" - można przetestować za pomocą komendy: python -m pip help. Jeśli wymaganie nie jest spełnione należy (w wierszu poleceń) wykonać komendę: 

python get-pip.py

W kolejnym kroku należy uruchomić wierz poleceń z poziomu głównego katalogu projektu i wykonać polecenie: 

pip install -r requirements.txt 

W kolejnym kroku należy przejść do podkatalogu /src i wykonać polecenie 

python main.py

UWAGA w niektórych systemach operacyjnych wymagane jest zastosowanie polecenia python3 zamiast python.

============================================================================

[English]

REST application for handling access to the MSIP system.
To download: "Code" - above the list of files and directories on the right and -> "Download Zip". Then, unpack the file saved on your computer (Windows: right mouse button -> Extract all, Linux: "sudo apt-get install unzip" and "unzip archive.zip") and go to the parent project directory.

Before running the application, make sure that Python is installed on your computer (recommended version 3.10.12) - test using the command (access to the command line on Windows in the File Browser: File -> Open Windows Powershell (hover and right) -> Open Windows Powershell as Administrator):

python --version

Then make sure that the default package management system "pip" is working - you can test it with the command: python -m pip help. If the requirement is not met, execute the command (in the command line):

python get-pip.py

In the next step, run the command line from the main project directory and execute the command:

pip install -r requirements.txt

In the next step, go to the /src subdirectory and execute the command

pythonmain.py

NOTE: Some operating systems require the python3 command instead of python.