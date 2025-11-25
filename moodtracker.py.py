import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime

MOOD_FILE = "simple_moods.json"

def load_moods():
    try:
        with open(MOOD_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_moods():
    with open(MOOD_FILE, "w") as f:
        json.dump(moods, f, indent=4)

def log_mood():
    mood = mood_var.get()
    if mood == "":
        messagebox.showwarning("No Selection", "Please select a mood.")
        return
    
    today = datetime.now().strftime("%Y-%m-%d")
    moods[today] = mood
    save_moods()
    messagebox.showinfo("Saved", f"Today's mood '{mood}' has been saved!")

def show_today():
    today = datetime.now().strftime("%Y-%m-%d")
    if today in moods:
        output_text.set(f"Today's mood: {moods[today]}")
    else:
        output_text.set("No mood logged today.")

def show_all():
    if not moods:
        output_text.set("No moods logged yet.")
        return
    
    text = "All logged moods:\n"
    for date, mood in moods.items():
        text += f"{date} → {mood}\n"
    
    output_text.set(text)

# ---------------- UI ---------------- #

# Load existing data
moods = load_moods()

# Main window
root = tk.Tk()
root.title("Simple Mood Tracker")
root.geometry("350x400")

# Mood Dropdown
mood_var = tk.StringVar()
mood_label = tk.Label(root, text="Select your mood:", font=("Arial", 12))
mood_label.pack(pady=10)

mood_dropdown = ttk.Combobox(root, textvariable=mood_var, state="readonly")
mood_dropdown["values"] = ["Happy", "Sad", "Angry", "Neutral", "Excited", "Anxious"]
mood_dropdown.pack(pady=5)

# Buttons
tk.Button(root, text="Log Mood", width=20, command=log_mood).pack(pady=10)
tk.Button(root, text="Show Today's Mood", width=20, command=show_today).pack(pady=5)
tk.Button(root, text="Show All Moods", width=20, command=show_all).pack(pady=5)

# Output Box
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, justify="left", font=("Arial", 10))
output_label.pack(pady=20)

root.mainloop()