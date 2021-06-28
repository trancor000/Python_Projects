
from tkinter import filedialog
from tkinter import *


class ParentWindow(Frame): 
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('File Browser')
        self.master.config(bg='lightgray')

        self.lblBrowse = Label(self.master, text='Browse', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblBrowse.grid(row=0, column=0,padx=(30,0), pady=(30,0))
        
        self.varFName = StringVar()
        self.varLName = StringVar()

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))


    def browse_button(self):
        dialog = wx.FileDialog(
            self, "Choose some files...", self._defaultDirectory, "",
            "TXT files (*.txt)|*.txt|PDF files (*.pdf)|*.pdf", wx.FD_OPEN|wx.FD_MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            paths = dialog.GetPaths()
        dialog.Destroy()
        


if __name__ == "__main__":
    root = Tk()
    browse_Button = Button(text="Browse", command=browse_button)
    browse_Button.grid(row=0, column=3)
    App = ParentWindow(root)
    root.mainloop()
