import tkinter as tk
from uploadfile import OpenFile
from log import LOG
from modeldown import Down
from size import SizePdf
import threading 
import action
class mainappTk(tk.Tk):
    def __init__(self):
        super().__init__()
        frame = tk.Frame(self)
        self.model = Down(frame)
        self.geometry('800x450')
        self.a = OpenFile(frame,label="ไฟล์ที่อยากจะปิด")
        self.a.grid(padx=3,column=0,row=0,sticky="w")
        self.b = OpenFile(frame,label="เก็บไฟล์",s=1)
        self.b.grid(padx=3,column=0,row=1,sticky="w")

        self.model.grid(column=0,row=2,sticky="wn")
        self.sizepdf = SizePdf(frame)
        self.sizepdf.grid(column=0,row=3,sticky="wn")
        self.button = tk.Button(frame,text="start",command=self.start,width=20)
        self.button.grid(padx=3,column=0,row=4,sticky="wn")
        frame2 = tk.Frame(self)
        self.log = LOG(frame2)
        self.log.grid(column=10,row=0,rowspan=20)
        
        frame.pack(side="left",anchor="n")
        frame2.pack()
    def doing(self,val,filename,savefiles,model,log,size):
        pdf = action.Pdf2Img(filename=filename,log=self.log,size=size)
        pdf.run()
        pr = action.predict(pdf.path(),val=val,model=model,log=log)
        pr.run()
        sa = action.savepdf(pr.path(),savefolder=savefiles,log=log)
        sa.run()
        clear =  action.Clear(pdf.path(),pr.path())
        clear.clear()
    def start(self):    
        if(len(self.b.path())==0 or len(self.a.path())==0):
            tk.messagebox.showwarning(title="Error", message="เลือกไฟล์")
            return
        elif self.model.Can() !=True:
            tk.messagebox.showwarning(title="Error", message="NONE MODEL")
            return
        print(self.a.path())
        me = threading.Thread(target=self.doing,args=[self.model.value(),self.a.path(),self.b.path(),self.model.show_selection(),self.log,self.sizepdf.value()])
        me.start()

app=mainappTk()
app.mainloop()