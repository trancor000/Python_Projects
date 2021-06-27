
import webbrowser
import tkinter
from tkinter import *


class ParentWindow(Frame):#basic tkinter code for GUI
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')
        
        self.varFName = StringVar()#defined attributes for ParentWindow class
        self.varLName = StringVar()
        self.varBText = StringVar()

        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblFName.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblLName.grid(row=1, column=0,padx=(30,0), pady=(30,0))

        self.lblBText = Label(self.master,text='Input text: ', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblBText.grid(row=2, column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1,padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1,padx=(30,0), pady=(30,0))

        self.txtBText = Entry(self.master,text=self.varBText, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBText.grid(row=2, column=1,padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) #button to send in the inputs given by the user
        self.btnSubmit.grid(row=3, column=1,padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=3, column=1,padx=(0,90), pady=(30,0), sticky=NE)
    

    def submit(self): #function to obtain the information 
        fn = self.varFName.get()
        ln = self.varLName.get()
        btext = self.varBText.get()
        
        def html(): #function to open up webpage in new tab
            f = open("basicHTML.html", "x")
            f.write("Stay tuned for our amazing summer sale!")
            f = open("basicHTML.html", "a")
            f.write(btext)

            #open and read the file after appending
            url = "basicHTML.html"
            webbrowser.open_new_tab(url)
        html()
        
        self.lblDisplay.config(text='Hello {} {}:'.format(fn,ln))

    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
