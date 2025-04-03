@echo off
echo -------------------------------
echo 🔧 HunterBot Setup (Python)
echo -------------------------------

REM Prüfen ob Python verfügbar ist
where python >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python wurde nicht gefunden!
    echo 🔗 Installiere Python 3.10 von https://www.python.org/downloads/release/python-3109/
    pause
    exit /b
)

REM Python-Version prüfen
python --version
for /f "tokens=2 delims= " %%v in ('python --version') do set version=%%v
set version10=%version:~0,4%
IF NOT "%version10%"=="3.10" (
    echo ❌ Gefundene Python-Version ist %version% – bitte stelle sicher, dass NUR Python 3.10 installiert ist!
    pause
    exit /b
)

REM Virtuelle Umgebung erstellen
echo ✅ Erstelle Umgebung...
python -m venv bot-env

REM Aktivieren
call bot-env\Scripts\activate.bat

REM Pip aktualisieren
echo 🔄 Aktualisiere pip...
python -m pip install --upgrade pip

REM TensorFlow & XGBoost installieren
echo 📦 Installiere TensorFlow & XGBoost...
pip install tensorflow xgboost joblib pandas

echo -------------------------------
echo ✅ Fertig! Starte den Bot mit:
echo    bot-env\Scripts\activate.bat
echo    python live_gui.py
echo -------------------------------
pause
