import tkinter as tk
from uploadfile import OpenFile
from log import LOG
from modeldown import Down
import threading 
import action
class mainappTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.model = Down(self)

        self.geometry('800x450')
        self.a = OpenFile(self,label="ไฟล์ที่อยากจะปิด")
        self.a.grid(padx=3,column=0,columnspan=10,row=0,sticky="w")
        self.b = OpenFile(self,label="เก็บไฟล์",s=1)
        self.b.grid(padx=3,column=0,columnspan=10,row=1,sticky="w")

        self.model.grid(column=0,row=2,sticky="wn")

        self.button = tk.Button(self,text="start",command=self.start,width=20)
        self.button.grid(padx=3,column=0,row=3,sticky="wn")
        self.log = LOG(self)
        self.log.grid(column=10,row=0,rowspan=20)
    def doing(self,val,filename,savefiles,model,log):
        pdf = action.Pdf2Img(filename=filename,log=self.log)
        pdf.run()
        pr = action.predict(pdf.path(),val=val,model=model,log=log)
        pr.run()
        sa = action.savepdf(pr.path(),savefolder=savefiles,log=log)
        sa.run()
    def start(self):    
        if(len(self.b.path())==0 or len(self.a.path())==0):
            tk.messagebox.showwarning(title="Error", message="เลือกไฟล์")
            return
        elif self.model.Can() !=True:
            tk.messagebox.showwarning(title="Error", message="NONE MODEL")
            return
        print(self.a.path())
        me = threading.Thread(target=self.doing,args=[self.model.value(),self.a.path(),self.b.path(),self.model.show_selection(),self.log])
        me.start()

app=mainappTk()
app.mainloop()