import tkinter as tk 
class LOG(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        fr = tk.Frame(self)
        fr.pack()
        self.label = tk.Label(fr,text="LOG")
        self.label.grid(column=0,row=0)
        self.log = tk.Text(self,width=50)
        self.log.pack()
    def add(self,text):
        self.log.insert(tk.END,text)
        self.log.see(tk.END)
    def index(self)->int:
        s= self.log.index("end-1c")
        return s
        