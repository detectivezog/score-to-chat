import tkinter as tk
from tkinter import messagebox
import winsound
import os

# Note frequencies (C3 to C5)
NOTES = {
    'C3': 131, 'C#3': 139, 'D3': 147, 'D#3': 156, 'E3': 165, 'F3': 175, 'F#3': 185, 'G3': 196, 'G#3': 208, 'A3': 220, 'A#3': 233, 'B3': 247,
    'C4': 262, 'C#4': 277, 'D4': 294, 'D#4': 311, 'E4': 330, 'F4': 349, 'F#4': 370, 'G4': 392, 'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 494,
    'C5': 523
}

class MelodyPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("J-Pop Melody Loader")
        self.score = []

        # Listbox for visual feedback
        self.listbox = tk.Listbox(root, height=12, width=40, font=("Courier", 10))
        self.listbox.pack(pady=20, padx=20)

        # Controls
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="📁 Load & Play .txt", width=18, bg="#dcf8c6", command=self.load_and_play).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="▶ Replay List", width=18, command=self.play_current).grid(row=0, column=1, padx=5)
        tk.Button(root, text="Clear List", command=lambda: [self.score.clear(), self.listbox.delete(0, tk.END)]).pack(pady=5)

    def load_and_play(self):
        filename = "melody_tabs.txt"
        if not os.path.exists(filename):
            messagebox.showerror("Error", "melody_tabs.txt not found!")
            return

        with open(filename, "r") as f:
            content = f.read().strip()
            self.score = content.split()
        
        self.listbox.delete(0, tk.END)
        for i, note in enumerate(self.score):
            self.listbox.insert(tk.END, f"{i+1:02d}: {note}")
        
        self.play_current()

    def play_current(self):
        if not self.score:
            return
        
        # Adjust playback speed here (300ms per note)
        for note in self.score:
            if note in NOTES:
                winsound.Beep(NOTES[note], 300)
            self.root.update() # Keeps the GUI responsive during playback

if __name__ == "__main__":
    root = tk.Tk()
    app = MelodyPlayer(root)
    root.mainloop()