import tkinter as tk
from tkinter import messagebox
import winsound

# Expanded Frequency Map: C3 to C5 (2 octaves)
NOTES = {
    'C3': 131, 'C#3': 139, 'D3': 147, 'D#3': 156, 'E3': 165, 'F3': 175, 'F#3': 185, 'G3': 196, 'G#3': 208, 'A3': 220, 'A#3': 233, 'B3': 247,
    'C4': 262, 'C#4': 277, 'D4': 294, 'D#4': 311, 'E4': 330, 'F4': 349, 'F#4': 370, 'G4': 392, 'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 494,
    'C5': 523
}

class FullPianoScorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sequencer (24+ Notes)")
        self.score = []

        # --- PIANO KEYBOARD SECTION ---
        piano_container = tk.Frame(root, bg="#333", padx=10, pady=10)
        piano_container.pack(pady=10)

        def create_octave(start_col, octave_label):
            # Black Keys (Top Row)
            blacks = [('C#', 1), ('D#', 3), (None, 5), ('F#', 7), ('G#', 9), ('A#', 11)]
            for name, rel_col in blacks:
                if name:
                    full_name = f"{name}{octave_label}"
                    btn = tk.Button(piano_container, text=full_name, bg="black", fg="white", 
                                    width=3, height=2, font=("Arial", 7),
                                    command=lambda n=full_name: self.add_note(n))
                    btn.grid(row=0, column=start_col + rel_col, columnspan=2)
            
            # White Keys (Bottom Row)
            whites = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
            for i, name in enumerate(whites):
                full_name = f"{name}{octave_label}"
                btn = tk.Button(piano_container, text=full_name, bg="white", fg="black", 
                                width=5, height=5, font=("Arial", 8, "bold"),
                                command=lambda n=full_name: self.add_note(n))
                btn.grid(row=1, column=start_col + (i * 2), columnspan=2)

        # Draw Octave 3, Octave 4, and the final C5
        create_octave(0, "3")
        create_octave(14, "4")
        tk.Button(piano_container, text="C5", bg="white", fg="black", width=5, height=5, 
                  font=("Arial", 8, "bold"), command=lambda: self.add_note("C5")).grid(row=1, column=28, columnspan=2)

        # --- LISTBOX ---
        self.listbox = tk.Listbox(root, height=8, width=50, font=("Courier", 10), bg="#f0f0f0")
        self.listbox.pack(pady=10)

        # --- CONTROL PANEL ---
        ctrl_frame = tk.Frame(root)
        ctrl_frame.pack(pady=10)

        # Top Row Controls
        tk.Button(ctrl_frame, text="▶ Play All", width=12, bg="#dcf8c6", command=self.play_all).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(ctrl_frame, text="🔊 Play Last", width=12, command=self.play_last).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(ctrl_frame, text="⌫ Backspace", width=12, bg="#ffcdd2", fg="#b71c1c", command=self.backspace).grid(row=0, column=2, padx=5, pady=5)

        # Bottom Row Controls
        tk.Button(ctrl_frame, text="💾 Export .txt", width=12, bg="#e3f2fd", command=self.export_txt).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(ctrl_frame, text="🗑 Clear All", width=12, command=self.clear_score).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(ctrl_frame, text="Quit", width=12, command=root.quit).grid(row=1, column=2, padx=5, pady=5)

    def add_note(self, note):
        self.score.append(note)
        self.listbox.insert(tk.END, f"Step {len(self.score):02d}: {note}")
        self.listbox.see(tk.END)
        winsound.Beep(NOTES[note], 250)

    def backspace(self):
        if self.score:
            self.score.pop()
            self.listbox.delete(tk.END)
        else:
            messagebox.showwarning("Empty", "No notes left to remove.")

    def play_last(self):
        if self.score:
            winsound.Beep(NOTES[self.score[-1]], 400)

    def play_all(self):
        for note in self.score:
            winsound.Beep(NOTES[note], 350)

    def clear_score(self):
        if messagebox.askyesno("Confirm", "Clear the entire melody?"):
            self.score.clear()
            self.listbox.delete(0, tk.END)

    def export_txt(self):
        if self.score:
            with open("melody_tabs.txt", "w") as f:
                f.write(" ".join(self.score))
            messagebox.showinfo("Exported", "Saved to melody_tabs.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = FullPianoScorer(root)

    root.mainloop()
