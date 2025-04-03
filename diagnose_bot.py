import os

print("🔍 Hunter Diagnose-Tool gestartet...")

required_files = [
    "HunterInstaller.exe",
    "run_bot.bat",
    "config.json",
    "model/lstm_model.h5",
    "model/xgb_model.pkl",
    "model/rl_trader.zip"
]

all_found = True

for file in required_files:
    if not os.path.exists(file):
        print(f"❌ FEHLT: {file}")
        all_found = False
    else:
        print(f"✅ OK: {file}")

if all_found:
    print("\n✅ Alles sieht gut aus. Du bist bereit zum Jagen!")
else:
    print("\n⚠️ Bitte überprüfe die fehlenden Dateien oben.")
