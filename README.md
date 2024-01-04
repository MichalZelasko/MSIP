# MSIP
[Polski]
REST application to handle access to MSIP system.
Przed uruchomieniem aplikacji należy upewnic się, że na komputerze zainstalowany jest Python (wersja zalecane 3.10.12) - test za pomoca komendy python --version
Następnie należy upewnic się, że działa domyslny system zarządzania pakietami "pip" - można przetestować za pomocą komendy: python -m pip help. Jeśli wymaganie nie jest spełnione należy (w wierszu poleceń) wykonać komendę: python get-pip.py
W kolejnym kroku należy uruchomić wierz poleceń z poziomu głównego katalogu projektu i wykonać polecenie: pip install -r requirements.txt 
W kolejnym kroku należy przejść do podkatalogu /src i wykonać polecenie python main.py

UWAGA w niektórych systemach operacyjnych wymagane jest zastosowanie polecenia python3 zamiast python.

[English]
REST application for handling access to the MSIP system.
Before running the application, make sure that Python (version 3.10.12) is installed on your desktop computer - test using the python --version command
You need to make sure that the default package management system "pip" is working - you can check with the commands: python -m pip help. If the requirement is necessary, please connect (in the base line) the command correctly: python get-pip.py
In this step, use the command from the main project and the command: pip install -r requirements.txt
In this step, go to the /src subdirectory and execute the python main.py command

NOTE in some cases provided, the python3 command is used instead of python.