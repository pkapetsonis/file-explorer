#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter.ttk import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
working_path = os.getcwd()
files = os.listdir(working_path)

program_path = os.path.dirname(__file__)
print(working_path)
print(files)

ICONS_SIZE = (48, 48)


window = tk.Tk()
window.geometry("525x500")
window.config(bg='#919191') 

#scrollbar--start--




container = ttk.Frame(window)
canvas = tk.Canvas(container, bg='#919191')
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.config(bg='#919191')

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox('all')
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

container.pack(fill=tk.BOTH, expand=True)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


cheat_label = tk.Label(scrollable_frame, text=' '*500,fg='black', bg='#919191', font=('Consolas', 1))
cheat_label.pack()

#scrollbar--end--



class DirectoryComponent(tk.Frame):
    

    def __init__(self, master, filename, file_path, working_path, mode):
        super().__init__(master, bg="grey", highlightbackground='black', highlightthickness=3)
        
        
        
        size = os.path.getsize(file_path)
        size_type = 'Bytes'

        if size > 1024:
            size = size / 1024
            size_type = 'kb'
        if size > 1024:
            size = size / 1024
            size_type = 'mb'

        self.filesize = '{:.1f}:{}'.format(size, size_type)
        selected_photo = icon_file

        if os.path.isfile(filename):
            selected_photo = icon_file
    
        elif os.path.isdir(filename):
            selected_photo = icon_folder
            self.filesize = ''

        self.working_path = working_path
        self.filename = filename 
        self.photo = selected_photo
        self.file_path = file_path
        if mode == 1:
            self.make_file_ui()
            print('1')
        elif mode == 2:
            self.extras_creator()
            print('2')
    
    def make_file_ui(self):
        self.photo_button = tk.Label(self, image=self.photo, border=0)
        self.photo_button.pack(side=tk.LEFT)

        self.name_label = tk.Label(self, text=self.filename, bg='grey', fg='black', font = ('UbuntuMono', 20))
        self.name_label.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True,  padx=10, pady=10)

        self.size_label = tk.Label(self, text=str(self.filesize), bg='grey', font=('UbuntuMono', 15))
        self.size_label.pack(side=tk.RIGHT)
        self.bind('<Double-Button-1>', self.onclick)

        #self.type_label = tk.Label(self, text=self.filetype, highlightthickness=3, highlightbackground="orange", bg='grey', fg='black', font=('Consolas', 15))
        #self.type_label.pack(side=tk.RIGHT)
    
    def extras_creator(self):
        print('22')
        return_button = tk.Button(scrollable_frame, border=1, text='<==', bg='#919191', command=self.last_path_tool, font=('Consolas', 16))
        return_button.pack(side=tk.TOP, anchor=tk.W)
        working_dir_label = tk.Label(scrollable_frame, bg='#919191', text=self.working_path, font=('Consolas', 14))
        working_dir_label.pack(side=tk.TOP)
    

    def onclick(self, event):
        print(self.filename, 'clicked')
        if os.path.isdir(self.filename):
            clicked_folder_path = self.file_path
            print("new path: ", clicked_folder_path)
            os.chdir(clicked_folder_path)
            refresher(self.filename, self.file_path, clicked_folder_path)
    

    def last_path_tool(self):
        last_path_list = os.path.split(self.working_path)
        last_path = os.path.join(*map(str, last_path_list[:-1]))
        os.chdir(last_path)
        refresher(self.filename, self.file_path, last_path)
    
    






           
            
def refresher(filename, file_path, clicked_folder_path):
    global scrollable_frame
    
    print(f"refresher: {filename=} {file_path=} {clicked_folder_path=}")

    files = os.listdir(clicked_folder_path)
    

    for w in scrollable_frame.winfo_children():
        w.destroy()

    extra_frame1 = DirectoryComponent(scrollable_frame, 'test', file_path, working_path, 2)
    extra_frame1.pack(side=tk.TOP)
    
    

    cheat_label = tk.Label(scrollable_frame, text=' '*500,fg='black', bg='#919191', font=('Consolas', 1))
    cheat_label.pack(fill=tk.BOTH, expand=True)
    
    
    for filename in files:
        new_file_path = os.path.join(clicked_folder_path, filename)
        print('filename:',  filename)
        
        
        
        
        file_label1 = DirectoryComponent(scrollable_frame, filename, new_file_path, clicked_folder_path, 1)
        file_label1.pack(fill=tk.X, pady=3)
    



            



#files = [f'test_file{i}' for i in range(5)]


img = Image.open(os.path.join(program_path, 'assets/file_image.png'))
img = img.resize(ICONS_SIZE, Image.ANTIALIAS)
icon_file = ImageTk.PhotoImage(img)

img = Image.open(os.path.join(program_path, r'assets/folder_image.png'))
img = img.resize(ICONS_SIZE, Image.ANTIALIAS)
icon_folder = ImageTk.PhotoImage(img)

extras_frame = DirectoryComponent(scrollable_frame, 'test', working_path, working_path, 2)
extras_frame.pack(side=tk.TOP)


for filename in files:
    
    file_path = '{}/{}'.format(working_path, filename)


    file_label1 = DirectoryComponent(scrollable_frame, filename, file_path, working_path, 1)
    file_label1.pack(fill=tk.X, pady=3)

        

window.mainloop()
