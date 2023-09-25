#!/usr/bin/env python3

import tkinter as tk

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os

# class FrontPage:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("TALOS Blind Code")
        

#         self.label = tk.Label(root, text="Welcome to Secure Text Editor", font=("Helvetica", 18))
#         self.label.pack(fill=BOTH, expand=YES)

#         self.start_button = tk.Button(root, text="Start", command=self.open_secure_text_editor)
#         self.start_button.pack()

#     def open_secure_text_editor(self):
#         self.root.destroy()  
#         secure_text_editor = tk.Tk()
#         editor = SecureTextEditor(secure_text_editor)
#         secure_text_editor.mainloop()

from PIL import Image, ImageTk

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title("TALOS Blind Code")
        self.set_ubuntu_application_name("TALOS Blind Code")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.background_image = Image.open("blind.jpg")
        self.background_image = self.background_image.resize((screen_width, screen_height), Image.ANTIALIAS) 
        self.bg_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.start_button = tk.Button(self.root, text="Start", command=self.open_secure_text_editor)
        self.start_button.place(relx=0.5, rely=0.5, anchor="center")

    def set_ubuntu_application_name(self, name):
        try:
            self.root.wm_attributes("-name", name)
        except tk.TclError:
            pass

    def open_secure_text_editor(self):
        self.root.destroy()  
        secure_text_editor = tk.Tk()
        editor = SecureTextEditor(secure_text_editor)
        secure_text_editor.mainloop()


class SecureTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("TALOS Blind Code") 
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        
        self.root.geometry(f"{screen_width}x{screen_height}")
        # self.background_image = Image.open("blind.jpg")
        # self.background_image = self.background_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.ANTIALIAS) 
        # self.bg_photo = ImageTk.PhotoImage(self.background_image)
        # self.background_label = tk.Label(self.root, image=self.bg_photo)
        # self.background_label.place(relwidth=1, relheight=1)
        self.text = tk.Text(self.root, height=40, width=100)
        self.text = tk.Text(self.root, wrap="none")
        self.text.pack(padx=10, pady=10)
        self.text.pack(fill=BOTH, pady=10, expand=YES)
        self.text.configure(bg="#666699")
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.run_button = tk.Button(self.root, text="Run", command=self.run_in_terminal)
        self.run_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.termf = Frame(root, height=200, width=600)
        self.termf.pack(padx=10, pady=10)
        self.termf.pack(fill=BOTH, pady=10, expand=YES)
        self.wid = self.termf.winfo_id()
        os.system('xterm -into %d -hold -geometry 1000x500 -sb -e "cd ~ && bash" &' % self.wid)
        
        self.footer = tk.Label(self.root, text="Designed and developed by Abinash Lingan K. Github@abinashlingank")
        self.footer.pack()

        self.actual_text = ""
        self.text.bind("<Key>", self.handle_key_event)
        self.text.bind("<BackSpace>", self.delete_previous_character)

        self.last_saved_directory = os.path.expanduser("~")
        self.last_saved_file_path = None
        
          

    def handle_key_event(self, event):
        self.actual_text += event.char
        current_index = self.text.index(tk.INSERT)  
        previous_index = self.text.index(f"{current_index} - 1 chars")
        self.text.replace(previous_index, current_index, "$")
        #return "break"

    def delete_previous_character(self, event):
        if self.actual_text:
            self.actual_text = self.actual_text[:-1]  
            current_index = self.text.index(tk.INSERT)
            previous_index = self.text.index(f"{current_index} - 1 chars")
            self.text.delete(previous_index)
        return "break" 
          
    def save_file(self):
        text_content = self.actual_text.replace("$", "")
        initial_dir = os.path.expanduser("~")
        file_path = filedialog.asksaveasfilename(initialdir=initial_dir, filetypes=[("Python files", "*.py"),("CPlusPlus", "*.cpp"),("Java", ".java")])

        if file_path:
            self.last_saved_directory = os.path.dirname(file_path)
            self.last_saved_file_path = file_path

            with open(file_path, "w") as file:
                file.write(text_content)
            print("File saved successfully.")

    def run_in_terminal(self):
        if self.last_saved_file_path:
            if self.last_saved_file_path.endswith(".py"):
                command = f'python3 "{self.last_saved_file_path}"'
                os.system(f'xterm -into {self.wid} -hold -e "{command}" &')
            elif self.last_saved_file_path.endswith(".cpp"):
                command = f'g++ "{self.last_saved_file_path}" -o output && ./output'
                os.system(f'xterm -into {self.wid} -hold -e "{command}" &')
            else:
                filename = os.path.basename(self.last_saved_file_path)
                dirpath = os.path.dirname(self.last_saved_file_path)
                command = f'javac "{self.last_saved_file_path}" && cd {dirpath} && java "{filename[:-5]}"'
                os.system(f'xterm -into {self.wid} -hold -e "{command}" &')


        


if __name__ == "__main__":
    root = tk.Tk()
    front_page = FrontPage(root)
    root.mainloop()

