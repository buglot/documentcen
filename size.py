import tkinter as tk

class SizePdf(tk.Frame):
    def __init__(self, master = None,):
        super().__init__(master)
        frame = tk.Frame(self)
        frame.grid(column=0,row=1)
        self.label1=tk.Label(frame,text="ขนาด pdf:")
        self.label1.pack(side="left")
        self.slider = tk.Scale(frame, from_=1, to=10, resolution=1,orient="horizontal" ,command=self.update_value)
        self.slider.set(4)
        self.slider.pack()
        self.value_label = tk.Label(frame, text="Value: 0.00 (x0)")
        self.value_label.pack()
    def update_value(self,val):
        self.value_label.config(text=f"Value: {float(val):.2f} (x{int(float(val))})")
    def value(self)->int:
        return int(self.slider.get())
