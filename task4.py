import tkinter as tk
from datetime import datetime

LOG_FILE = "keystroke_log.txt"

def log_key(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = event.char if event.char else f"[{event.keysym}]"
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {key}\n")

root = tk.Tk()
root.title("Keyboard Input Logger (Consent-Based)")

label = tk.Label(
    root,
    text="Type inside the box below.\nKeystrokes are logged only within this application.",
    font=("Arial", 10)
)
label.pack(pady=10)

text_area = tk.Text(root, width=50, height=10)
text_area.pack(padx=10, pady=10)

text_area.bind("<Key>", log_key)

root.mainloop()
