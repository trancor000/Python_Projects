from tkinter import filedialog
from tkinter import *

DEFAULT_FILE_PATH = r"C:\Users\m0pxnn\Documents\Python"#Creating the folder path for the browse
FOLDER_PATH = r"C:\Users\Owner\OneDrive\Documents\GitHub\Python_Projects\Folder mods"
filename = "<NOTHING SELECTED>"
folderName = "<Folder not selected>"

def BrowseDir():#function for browsing for folder
    folderName = filedialog.askdirectory(initialdir=DEFAULT_FILE_PATH, title="Select folder")
    print("Folder selected: ", folderName)
    lblFilename['text'] = "Folder selected: " + folderName

def CheckDaily():
    folderName = filedialog.askdirectory(initialdir=FOLDER_PATH, title="Folder mods",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print("Folder selected: Folder mods")
    lblFilename['text'] = "File selected: Folder mods"


#############################################
root = Tk()

btnBrowseDir = Button(root, text="Browse Folder", command=BrowseDir)#button to be used to browse
btnBrowseDir.pack()

lblFilename = Label(root, text=filename, width=50, padx=2, pady=2, bd=2, relief=RIDGE  )
lblFilename.pack()

btnCheckDaily = Button(root, text="Check Mods Daily", command=CheckDaily)#button to be used to check
btnCheckDaily.pack()

lblFoldername = Label(root, text=Foldername, width=50, padx=2, pady=2, bd=2, relief=RIDGE  )
lblFoldername.pack()

root.mainloop()
