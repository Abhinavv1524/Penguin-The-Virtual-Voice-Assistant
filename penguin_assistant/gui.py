# gui.py

import tkinter as tk
from tkinter import ttk

def create_gui(activate_callback):
    root = tk.Tk()
    root.title("Penguin Assistant")

    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

    frame = ttk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=(20, 10))

    emoji_label = ttk.Label(frame, text="🤖", font=("Segoe UI Emoji", 48))
    emoji_label.pack(pady=(0, 10))

    text_label = ttk.Label(frame, text="Welcome to Your Personal Assistant", font=("Helvetica", 12))
    text_label.pack(pady=(0, 10))

    button = ttk.Button(frame, text="Activate Penguin 🐧", command=activate_callback)
    button.pack(pady=(0, 10))

    root.mainloop()
