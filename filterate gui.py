import tkinter as tk
from tkinter import filedialog, messagebox
import os

def get_unique_path(path):
    if not os.path.exists(path):
        return path

    base, ext = os.path.splitext(path)
    i = 1
    while True:
        new_path = f"{base}({i}){ext}"
        if not os.path.exists(new_path):
            return new_path
        i += 1


def select_input():
    path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, path)


def select_output():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, path)


def run_filter():
    input_path = input_entry.get()
    output_path = output_entry.get()

    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select input and output files.")
        return

    if not os.path.isfile(input_path):
        messagebox.showerror("Error", "Input file not found.")
        return

    try:
        min_len = int(min_entry.get())
    except:
        messagebox.showerror("Error", "Minimum length must be a number.")
        return

    output_path = get_unique_path(output_path)

    total = 0
    kept = 0

    try:
        with open(input_path, "r", errors="ignore") as fin, open(output_path, "w") as fout:
            for line in fin:
                total += 1
                line = line.strip()

                if len(line) >= min_len:
                    kept += 1
                    fout.write(line + "\n")

        messagebox.showinfo(
            "Done",
            f"Filtering complete!\n\n"
            f"Total: {total}\n"
            f"Kept: {kept}\n"
            f"Removed: {total - kept}\n\n"
            f"Saved to:\n{output_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Text Filter Tool")
root.geometry("500x250")

tk.Label(root, text="Input File").pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()
tk.Button(root, text="Browse", command=select_input).pack()

tk.Label(root, text="Output File").pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
tk.Button(root, text="Browse", command=select_output).pack()

tk.Label(root, text="Minimum Length").pack()
min_entry = tk.Entry(root)
min_entry.insert(0, "1")
min_entry.pack()

tk.Button(root, text="Run Filter", command=run_filter, bg="green", fg="white").pack(pady=10)

root.mainloop()