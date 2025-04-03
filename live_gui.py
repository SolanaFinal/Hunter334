
import tkinter as tk
from sentiment_loop import get_latest_sentiment
import time
import threading

class BotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HunterBot Control Center")
        self.root.geometry("800x600")
        self.root.configure(bg="#121212")

        self.log_text = tk.Text(self.root, height=30, width=100, bg="#1e1e1e", fg="#00ff5f", insertbackground="#00ff5f")
        self.log_text.pack(pady=20)

        self.update_trade_log_loop()

    def update_trade_log_loop(self):
        def loop():
            while True:
                try:
                    sentiment_score, headlines, tech, predicted_price, action_class = get_latest_sentiment()

                    self.log_text.insert(tk.END, f"[SENTIMENT] Score: {sentiment_score}\n")
                    for hl in headlines:
                        self.log_text.insert(tk.END, f"[NEWS] {hl}\n")

                    if tech:
                        self.log_text.insert(tk.END, f"[TECHNICAL] RSI: {tech['rsi']} | MACD: {tech['macd']} | BB-High: {tech['bb_high']} | BB-Low: {tech['bb_low']} | Price: {tech['price']}\n")

                    self.log_text.insert(tk.END, f"[LSTM] Predicted Price: {predicted_price}\n")

                    action = "BUY" if action_class == 1 else "SELL"
                    self.log_text.insert(tk.END, f"[TRADE] Suggested Action: {action}\n")
                    self.log_text.insert(tk.END, "-"*70 + "\n")

                    self.log_text.see(tk.END)
                except Exception as e:
                    self.log_text.insert(tk.END, f"[ERROR] {str(e)}\n")
                    self.log_text.see(tk.END)
                time.sleep(10)

        t = threading.Thread(target=loop)
        t.daemon = True
        t.start()

def start_gui():
    root = tk.Tk()
    app = BotGUI(root)
    root.mainloop()

print("Starte Hunter...")
start_gui()
