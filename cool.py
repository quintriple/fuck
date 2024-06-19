import tkinter as tk
from tkinter import simpledialog, messagebox

class PasswordUI:
    def __init__(self, root):
        self.root = root
        self.password = None
        self.toggle_states = {
            "AIM LOCK TOGGLE": False,
            "FLY HACK TOGGLE": False,
            "ANTI BAN": False,
        }

        self.ask_password()

    def ask_password(self):
        self.password = simpledialog.askstring("Set Password", "Please set a password:", show='*')
        confirm_password = simpledialog.askstring("Confirm Password", "Please confirm your password:", show='*')

        if self.password == confirm_password:
            self.main_ui()
        else:
            messagebox.showerror("Error", "Passwords do not match. Try again.")
            self.ask_password()

    def main_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # ASCII Art
        ascii_art = tk.Label(self.root, text="GRUBV2", font=("Courier", 18))
        ascii_art.pack()

        # Toggle Buttons
        for toggle in self.toggle_states:
            button = tk.Button(self.root, text=toggle.lower(), command=lambda t=toggle: self.toggle(t))
            button.pack(pady=5)

        # Add Cheats Button
        add_cheats_button = tk.Button(self.root, text="add cheats", command=self.add_cheats)
        add_cheats_button.pack(pady=5)

    def toggle(self, toggle):
        self.toggle_states[toggle] = not self.toggle_states[toggle]
        button = [child for child in self.root.winfo_children() if child.cget("text").lower() == toggle.lower()][0]
        button.config(text=toggle if self.toggle_states[toggle] else toggle.lower())

    def add_cheats(self):
        messagebox.showinfo("Add Cheats", "Cheats added!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("GRUBV2")
    app = PasswordUI(root)
    root.mainloop()