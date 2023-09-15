import os
import shutil
import tkinter as tk
from tkinter import filedialog


def move_file(source_dir, target_dir, filename):
    source_path = os.path.join(source_dir, filename)
    target_path = os.path.join(target_dir, filename)
    shutil.move(source_path, target_path)


def move_files_by_date(source_dir, target_dir):
    for current_dir, dirs, files in os.walk(source_dir):
        for filename in files:
            source_path = os.path.join(current_dir, filename)
            target_path = os.path.join(target_dir, filename)

            if os.path.exists(target_path):
                source_mtime = os.path.getmtime(source_path)
                target_mtime = os.path.getmtime(target_path)

                if source_mtime > target_mtime:
                    move_file(current_dir, target_dir, filename)
            else:
                move_file(current_dir, target_dir, filename)


def browse_source_directory():
    source_directory = filedialog.askdirectory()
    source_dir_entry.delete(0, tk.END)
    source_dir_entry.insert(0, source_directory)


def browse_target_directory():
    target_directory = filedialog.askdirectory()
    target_dir_entry.delete(0, tk.END)
    target_dir_entry.insert(0, target_directory)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Move Files by Date")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    source_label = tk.Label(frame, text="Исходная директория:")
    source_label.grid(row=0, column=0, sticky="w")

    source_dir_entry = tk.Entry(frame, width=50)
    source_dir_entry.grid(row=0, column=1)

    browse_source_button = tk.Button(frame, text="Обзор", command=browse_source_directory)
    browse_source_button.grid(row=0, column=2)

    target_label = tk.Label(frame, text="Целевая директория:")
    target_label.grid(row=1, column=0, sticky="w")

    target_dir_entry = tk.Entry(frame, width=50)
    target_dir_entry.grid(row=1, column=1)

    browse_target_button = tk.Button(frame, text="Обзор", command=browse_target_directory)
    browse_target_button.grid(row=1, column=2)

    move_button = tk.Button(frame, text="Переместить файлы",
                            command=lambda: move_files_by_date(source_dir_entry.get(), target_dir_entry.get()))
    move_button.grid(row=2, column=1)

    root.mainloop()
