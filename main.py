#! /usr/bin/env python3
import os
import tkinter as tk
from tkinter.ttk import *
from PIL import Image
from PIL import ImageTk
working_path = os.getcwd()
files = os.listdir(working_path)

print(working_path)
print(files)

ICONS_SIZE = (48, 48)
#---------tk----------

class DirectoryComponent(tk.Frame):

    def __init__(self, master, filename, filesize, selected_photo):
        super().__init__(master, bg="grey", highlightbackground='black', highlightthickness=3)
        self.filename = filename 
        self.filesize = filesize
        #self.filetype = filetype
        self.photo = selected_photo
        self.make_file_ui()
    
    def make_file_ui(self):
        self.photo_button = tk.Label(self, image=self.photo, border=0)
        self.photo_button.pack(side=tk.LEFT)

        self.name_label = tk.Label(self, text=self.filename, highlightbackground="orange", highlightthickness=3 ,bg='grey', fg='black', font = ('UbuntuMono', 20))
        self.name_label.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True,  padx=10, pady=10)

        self.size_label = tk.Label(self, text=str(self.filesize), bg='grey', font=('UbuntuMono', 15), highlightthickness=3, highlightbackground="orange")
        self.size_label.pack(side=tk.RIGHT)
        self.bind('<Double-Button-1>', self.onclick)

        #self.type_label = tk.Label(self, text=self.filetype, highlightthickness=3, highlightbackground="orange", bg='grey', fg='black', font=('Consolas', 15))
        #self.type_label.pack(side=tk.RIGHT)

    def onclick(self, event):
        print(self.filename, 'clicked')


window = tk.Tk()
window.geometry("500x500")
window.config(bg='#919191')
#files = [f'test_file{i}' for i in range(5)]


img = Image.open(r'assets/file_image.png')
img = img.resize(ICONS_SIZE, Image.ANTIALIAS)
icon_file = ImageTk.PhotoImage(img)

img = Image.open(r'assets/folder_image.png')
img = img.resize(ICONS_SIZE, Image.ANTIALIAS)
icon_folder = ImageTk.PhotoImage(img)

for filename in files:
    file_path = '{}/{}'.format(working_path, filename)

    size = os.path.getsize(file_path)
    size_type = 'Bytes'

    if size > 1024:
         size = size / 1024
         size_type = 'kb'
         if size > 1024:
             size = size / 1024
             size_type = 'mb'

    filesize = '{:.1f}:{}'.format(size, size_type)

    if os.path.isfile(filename):
        selected_photo = icon_file
    
    elif os.path.isdir(filename):
        selected_photo = icon_folder


    


    file_label1 = DirectoryComponent(window, filename, filesize, selected_photo)
    file_label1.pack(fill=tk.X, pady=3)




window.mainloop()
