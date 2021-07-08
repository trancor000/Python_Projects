from tkinter import filedialog
from tkinter import *
import os
import shutil

DEFAULT_FILE_PATH = r"C:\Users\m0pxnn\Documents\Python"#Creating the folder path for the browse
FOLDER_PATH = r"C:\Users\Owner\OneDrive\Documents\GitHub\Python_Projects\Folder mods"


def BrowseDir():#function for browsing for folder
    folderName = filedialog.askdirectory(initialdir=DEFAULT_FILE_PATH, title="Select folder")
    sourceEntry.delete(0,END)
    sourceEntry.insert(END,folderName)
    

def BrowseDir2():
    folderName = filedialog.askdirectory(initialdir=FOLDER_PATH, title="Select folder")
    destEntry.delete(0,END)
    destEntry.insert(END,folderName)

def TransferFiles():
    source = sourceEntry.get()
    destination = destEntry.get()
    fileList = os.listdir(source)
    for i in fileList:
        shutil.move(source + i, destination)
        


#############################################
root = Tk()

btnBrowseDir = Button(root, text="Browse Folder", command=BrowseDir)#button to be used to browse
btnBrowseDir.pack()

lblFilename = Label(root, text="filename", width=50, padx=2, pady=2, bd=2, relief=RIDGE  )
lblFilename.pack()

btnBrowseDir2 = Button(root, text="Destination Folder", command=BrowseDir2)#button to be used to check
btnBrowseDir2.pack()

lblFoldername = Label(root, text="Foldername", width=50, padx=2, pady=2, bd=2, relief=RIDGE  )
lblFoldername.pack()

sourceEntry = Entry(root)
sourceEntry.pack()

destEntry = Entry(root)
destEntry.pack()

btnTransfer = Button(root, text="Transfer Files", command=TransferFiles)
btnTransfer.pack()

root.mainloop()
