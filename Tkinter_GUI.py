import tkinter as tk
import os
from tkinter import filedialog
from Text_extractor import extract_text
from subprocess import Popen

window = tk.Tk()


def execute_extraction():
    page_number = entry_pg.get()
    filename = entry_filename.get()

    extract_text(page_number, filename)

def file_select():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        entry_filename.delete(0, tk.END)
        entry_filename.insert(0, file_name)

# Adding a widget - label
label = tk.Label(text="PDF Text Extractor",
                 foreground="purple",
                 background="white",
                 width=20,
                 height=3)
label.grid(row=0, column=0, columnspan=2)

# Adding a widget - button

button = tk.Button(text="Execute",
                   width=25,
                   height=3,
                   bg="blue",
                   fg="black",
                   command=execute_extraction)
button.grid(row=1, column=0, columnspan=2)

# Adding a widget - button (file selection)

button_file = tk.Button(text="Select\nFile",
                        width=3,
                        height=2,
                        bg="green",
                        fg="grey",
                        command=file_select)
button_file.grid(row=4, column=3)

# Adding a widget - entry

pg_label = tk.Label(window, text="Page Number")
entry_pg = tk.Entry(fg="black", bg="yellow", width=20)


filename_label = tk.Label(window, text="File Name")
entry_filename = tk.Entry(fg="black", bg="yellow", width=20)

pg_label.grid(row=3, column=0)
entry_pg.grid(row=3, column=1)

filename_label.grid(row=4, column=0)
entry_filename.grid(row=4, column=1)

# run the Tkinter event loop (to listen for events)
window.mainloop()
