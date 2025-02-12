import tkinter as tk
import tkinter.filedialog as fd
import tkinter.filedialog
class OpenFile(tk.Frame):
    def __init__(self, master = None,label="",s=0):
        super().__init__(master)
        self.label = tk.Label(self,text=label)
        self.barEntry = tk.Entry(self,width=50)
        self.label.grid(column=0,row=0,sticky="w")
       
        self.barEntry.grid(column=0,columnspan=10,row=1,sticky="we")
       

        if(s==0):
            self.button = tk.Button(self,text="OpenFile",command=self.show,width=8)
            self.button.grid(column=10,row=1,sticky="e")
        else:
            self.button = tk.Button(self,text="Save",command=self.showsave,width=8)
            self.button.grid(column=10,row=1,sticky="e")
    def show(self):
        filetypes = (
            ('pdf', '*.pdf'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        self.barEntry.delete(0,tk.END)
        self.barEntry.insert(0,filename)
    def showsave(self):
        filetypes = (
            ('pdf files', '*.pdf'),
            ('All files', '*.*')
        )

        filename = fd.asksaveasfilename(
            title='Save File',
            initialdir='/',
            filetypes=filetypes)
        if filename.endswith(".pdf") == False:
            filename+=".pdf"
        self.barEntry.delete(0,tk.END)
        self.barEntry.insert(0,filename)
    def path(self)->str:
        return self.barEntry.get()
