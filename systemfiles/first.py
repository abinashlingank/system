#!/usr/bin/env python3

import tkinter as tk

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os



from PIL import Image, ImageTk

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title("TALOS Blind Code")
        self.set_ubuntu_application_name("TALOS Blind Code")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.background_image = PhotoImage(file="1st_page.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.coni = PhotoImage(file="continue.png")
        self.conf = tk.Frame(self.root, width=255, height=68)
        self.conf.place(x=1497, y=849)
        self.con=tk.Button(self.conf, image=self.coni, command=self.open_2nd_page, borderwidth=0, bg="#012136")
        self.con.place(x=0, y=0, relwidth=1, relheight=1)

    def set_ubuntu_application_name(self, name):
        try:
            self.root.wm_attributes("-name", name)
        except tk.TclError:
            pass

    def open_2nd_page(self):
        self.root.destroy()  
        second_page = tk.Tk()
        second_page.attributes('-fullscreen', True)
        icon = PhotoImage(file="save.png")
        second_page.iconphoto(True, icon)
        editor = RulePage(second_page)
        second_page.mainloop()


class RulePage:
    def __init__(self, root):
        self.root = root
        self.root.title("TALOS Blind Code")
        self.set_ubuntu_application_name("TALOS Blind Code")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.background_image = PhotoImage(file="2nd_page.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.starti = PhotoImage(file="start.png")
        self.startf = tk.Frame(self.root, width=261, height=62)
        self.startf.place(x=1502, y=856)
        self.start=tk.Button(self.startf, image=self.starti, command=self.open_secure_text_editor, borderwidth=0, bg="#012136")
        self.start.place(x=0, y=0, relwidth=1, relheight=1)
        self.backi = PhotoImage(file="back.png")
        self.backf = tk.Frame(self.root, width=261, height=62)
        self.backf.place(x=156, y=856)
        self.back=tk.Button(self.backf, image=self.backi, command=self.back_btn, borderwidth=0, bg="#012136")
        self.back.place(x=0, y=0, relwidth=1, relheight=1)
        

    def set_ubuntu_application_name(self, name):
        try:
            self.root.wm_attributes("-name", name)
        except tk.TclError:
            pass

    def open_secure_text_editor(self):
        self.root.destroy()  
        secure_text_editor = tk.Tk()
        secure_text_editor.attributes('-fullscreen', True)
        icon = PhotoImage(file="save.png")
        secure_text_editor.iconphoto(True, icon)
        editor = SecureTextEditor(secure_text_editor)
        secure_text_editor.mainloop()

    def back_btn(self):
        self.root.destroy()
        back_btn = tk.Tk()
        back_btn.attributes('-fullscreen', True)
        icon = PhotoImage(file="save.png")
        back_btn.iconphoto(True, icon)
        back = FrontPage(back_btn)
        back_btn.mainloop()


class SecureTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("TALOS Blind Code") 
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.background_image = PhotoImage(file="3rd_page.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.texti = PhotoImage(file="text.png")
        self.textf = tk.Label(self.root, image=self.texti ,width=1289, height=329, borderwidth=0)
        self.textf.place(x=339, y=231)
        self.textbi = PhotoImage(file="textb.png")
        self.text = tk.Text(self.textf, width=329, height=1289, bg = "#36475A")#, bg="#FFFFFF00"
        self.text.place(x=0, y=0,relwidth=1, relheight=1)
        self.actual_text = ""
        self.text.bind("<Key>", self.handle_key_event)
        self.text.bind("<BackSpace>", self.delete_previous_character)

        self.savei = PhotoImage(file="save.png")
        self.savef = tk.Frame(self.root, width=125, height=30)
        self.savef.place(x=747, y=596)
        self.save=tk.Button(self.savef, image=self.savei, command=self.save_file, borderwidth=0, bg="#012136")
        self.save.place(x=0, y=0, relwidth=1, relheight=1)

        self.runi = PhotoImage(file="run.png")
        self.runf = tk.Frame(self.root, width=125, height=30)
        self.runf.place(x=1048, y=596)
        self.run=tk.Button(self.runf, image=self.runi, command=self.run_in_terminal, borderwidth=0, bg="#012136")
        self.run.place(x=0, y=0, relwidth=1, relheight=1)
        self.backi = PhotoImage(file="back.png")
        self.backf = tk.Frame(self.root, width=261, height=62)
        self.backf.place(x=158, y=845)
        self.back=tk.Button(self.backf, image=self.backi, command=self.back_btn, borderwidth=0, bg="#012136")
        self.back.place(x=0, y=0, relwidth=1, relheight=1)
        self.termf = tk.Frame(self.root, width = 865, height = 303)
        self.termf.place(x=527, y=670)
        self.wid = self.termf.winfo_id()
        os.system('xterm -into %d -hold -geometry 1000x500 -sb -e "cd ~ && bash" &' % self.wid)
        self.footeri = PhotoImage(file="footer.png")
        self.footer = tk.Label(self.root, image=self.footeri, width = 812, height=49, borderwidth=0)
        self.footer.place(x=557, y=977)
        self.last_saved_directory = os.path.expanduser("~")
        self.last_saved_file_path = None
        
          

    def handle_key_event(self, event):
        self.actual_text += event.char
        current_index = self.text.index(tk.INSERT)  
        previous_index = self.text.index(f"{current_index} - 1 chars")
        self.text.replace(previous_index, current_index, "*")
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
            print(".")

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

    def back_btn(self):
        self.root.destroy()
        back_btn = tk.Tk()
        back_btn.attributes('-fullscreen', True)
        icon = PhotoImage(file="save.png")
        back_btn.iconphoto(True, icon)
        back = FrontPage(back_btn)
        back_btn.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    icon = PhotoImage(file="save.png")
    root.iconphoto(True, icon)
    front_page = FrontPage(root)
    root.mainloop()

