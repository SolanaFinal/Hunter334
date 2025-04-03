@echo off
echo 🚀 Starte HunterBot...
call bot-env\Scripts\activate.bat

REM GUI starten
start "HunterBot GUI" cmd /k python live_gui.py

REM Lernprozess starten
start "Lernprozess" cmd /k python learning_loop.py

echo ✅ HunterBot läuft!
