@echo off
echo Wiederherstellung der Modelle gestartet...

mkdir model

copy lstm_model.h5 model\
copy xgb_model.pkl model\
copy rl_trader.zip model\

echo ✅ Modelle wurden in den model-Ordner kopiert.
pause
