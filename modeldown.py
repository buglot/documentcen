import tkinter as tk
import os
class Down(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master) 
        self.fr = tk.Frame(self)
        label = tk.Label(self.fr,text="Model : ")
        label.pack(side="left")
        if os.path.exists(os.path.join("model"))!=True:
            os.mkdir("model")
        self.options = os.listdir("model")
        if len(self.options) == 0:
            self.options.append("None model")
       
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])
        self.buttonre = tk.Button(self.fr,text="reload",command=self.Reload_options)
        # Create the dropdown menu
        self.dropdown = tk.OptionMenu(self.fr, self.selected_option, *self.options)
        self.dropdown.pack(side="left")
        self.buttonre.pack(side="left")
        self.fr.grid(column=0,row=0)
        self.label1=tk.Label(self,text="ความมั่นใจที่วาดกล่อง(1.00 = 100%) :")
        self.label1.grid(column=0,row=2,columnspan=3)
        self.slider = tk.Scale(self, from_=0, to=1, resolution=0.01,orient="horizontal" ,command=self.update_value)
        self.slider.set(0.65)
        self.slider.grid(column=0,row=3)

        self.value_label = tk.Label(self, text="Value: 0.00 (0%)")
        self.value_label.grid(column=0,row=4)
    def update_value(self,val):
        self.value_label.config(text=f"Value: {float(val):.2f} ({int(float(val)*100)}%)")
    def value(self)->float:
        return self.slider.get()
    def show_selection(self):
            return self.selected_option.get()
    def Can(self)->bool:
            return self.selected_option.get() != "None model"
    def Reload_options(self):
            self.options = os.listdir("model")
            self.dropdown['menu'].delete(0, 'end')  # Clear current options
            for option in self.options:
                self.dropdown['menu'].add_command(label=option, command=tk._setit(self.selected_option, option))

            # Update the selected option to the first item of the new list
            self.selected_option.set(self.options[0])