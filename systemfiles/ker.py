#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog

class SecureTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("TALOS Blind Code")
        # root.attributes('-fullscreen', True)
        # self.root.geometry("1024x812") 
        self.text = tk.Text(self.root, height=40, width=100)
        self.text = tk.Text(self.root, wrap="none")
        self.text.pack(padx=10, pady=10)
        # self.text.config(insertbackground="red")
        self.text.configure(bg="blue")
        self.save_button = tk.Button(self.root, text="Save", command=self.save_file)
        self.save_button.pack(pady=5)
        self.actual_text = ""
        self.text.bind("<Key>", self.handle_key_event)  # Bind normal key presses
        self.text.bind("<BackSpace>", self.delete_previous_character)
        # self.text.bind("<Key>", self.handle_key_event)
        # self.text.unbind_all("<Key>")
        
          

    def handle_key_event(self, event):
        self.actual_text += event.char
        current_index = self.text.index(tk.INSERT)  # Get the current insertion cursor index
        previous_index = self.text.index(f"{current_index} - 1 chars")
        self.text.replace(previous_index, current_index, "$")
        # return "break"

    
    # def delete_previous_character(self, event):
    #     self.actual_text = self.actual_text[-1]
    #     current_index = self.text.index(tk.INSERT)  
    #     previous_index = self.text.index(f"{current_index} - 1 chars")  
    #     self.text.delete(previous_index, current_index)
    def delete_previous_character(self, event):
        if self.actual_text:
            self.actual_text = self.actual_text[:-1]  
            current_index = self.text.index(tk.INSERT)
            previous_index = self.text.index(f"{current_index} - 1 chars")
            # self.text.replace(previous_index, current_index, "*")
            # self.text.insert(current_index, "$")
            self.text.delete(previous_index, current_index)
            # self.text.delete(previous_index, current_index)
        # return "break" 
          
    def save_file(self):
        text_content = self.actual_text.replace("$", "")
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])

        if file_path:
            with open(file_path, "w") as file:
                file.write(text_content)
            print("File saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = SecureTextEditor(root)
    root.mainloop()

# import tkinter as tk
# from tkinter import filedialog
# from tkinter import PhotoImage

# class SecureTextEditor:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Secure Text Editor")
        
#         # Load the background image
#         self.bg_image = PhotoImage(file="overlay-image.png")  # Replace with your image file path

#         # Create a Canvas widget
#         self.canvas = tk.Canvas(self.root, width=800, height=600)  # Adjust width and height
#         self.canvas.pack()

#         # Display the background image on the Canvas
#         self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        
#         # Create the Text widget within the Canvas
#         self.text = tk.Text(self.canvas, height=40, width=100)
#         self.text.place(x=10, y=10)
#         self.text.configure(bg="black")  # Adjust position based on your design

#         self.save_button = tk.Button(self.root, text="Save", command=self.save_file)
#         self.save_button.pack(pady=5)
        
#         self.text.bind("<Key>", self.handle_key_event)
#         self.text.unbind_all("<Key>")
#         self.actual_text = ""

#     def handle_key_event(self, event):
#         self.actual_text += event.char
#         current_index = self.text.index(tk.INSERT)  # Get the current insertion cursor index
#         previous_index = self.text.index(f"{current_index} - 1 chars")
#         self.text.replace(previous_index, current_index, "$")

#     def save_file(self):
#         text_content = self.actual_text.replace("$", "")
#         file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

#         if file_path:
#             with open(file_path, "w") as file:
#                 file.write(text_content)
#             print("File saved successfully.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     editor = SecureTextEditor(root)
#     root.mainloop()