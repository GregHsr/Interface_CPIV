import os
import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar
import re

class Security:
    def __init__(self):
        self.path = os.getcwd()

    def check_tiffile(self, file):
        if file.endswith('.tif') == False:
            return False
        elif os.path.exists(file) == False or os.path.isabs(file) == False:
            return False
        else:
            return True
        
    def check_directory(self, directory):
        if os.path.isabs(directory) == False or os.path.isdir(directory) == False:
            return False
        else:
            return True
        
    def check_int(self, value):
        try:
            int(value)
            print(str(int(value)), value)
            print(str(int(value)) == str(value))
            if str(int(value)) != str(value):
                return False
            else:
                return True
        except ValueError:
            return False
        
    def check_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def check_string(self, value):
        if type(value) == str:
            return True
        else:
            return False
        
    def ask_validation(self, message):
        # Yes or no window
        answer = messagebox.askyesno('Validation', message)
        return answer
    
    def validate_int(self, new_value):
        if new_value == "":
            return True
        if re.fullmatch(r"-?\d+", new_value):
            return True
        else:
            messagebox.showwarning("Invalid input", "Please enter a valid integer.")
            return False

    def validate_float(self, new_value):
        if new_value == "": 
            return True
        try:
            float(new_value)  
            return True
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid float.")
            return False


    def show_help(self):
        # Create a new top-level window for help
        help_window = Toplevel(self.root)
        help_window.title("Help")

        help_text = Text(help_window, wrap="word", padx=10, pady=10)
        help_text.insert("1.0", self.get_help_text())  # Insert help text
        help_text.config(state="disabled")  # Make text read-only

        scrollbar = Scrollbar(help_window, command=help_text.yview)
        help_text.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        help_text.pack(expand=True, fill="both")

    def get_help_text(self):
        return ( 
            "Input_typedata : Deux images simples, Une image double, Séquence d'images double ou Sequence d'images simples \n"
            "Input_SEQDirname : Directory\n"
            "Input_SEQdebut : Integer\n"
            "Input_SEQinterImg : Integer\n"
            "Input_SEQinterPaire : Integer\n"
            "Input_Imgdouble : TIF image\n"
            "Input_ImgTWO1 : TIF image\n"
            "Input_ImgTWO2 : TIF image\n"
            "Input_Masque : YES / NO\n"
            "Input_TypeMasque : ONE / SEQUENCE\n"
            "Input_OneNameMasque : TIF image\n"
            "Input_SeqDirMasque : Directory\n"
            "CalculCPIV_meths : PIVDEFORM | PIVDECAL | PIVSIMPLE\n"
            "CalculCPIV_dimXYcell : Integers\n"
            "CalculCPIV_recouv : floats between 0 et 1 non compris, ex: 0,5 => recovery of 50%\n"
            "CalculCPIV_ROI : YES / NO\n"
            "CalculCPIV_ROIval : 4 integers: (x0, y0) for the top-left corner and (x1, y1) for the bottom-right corner, where x1>x0x1>x0 and y1>y0y1>y0.\n"
            "CalculCPIV_ConvTools : YES / NO\n"
            "CalculCPIV_FiltrePostCalcul : YES / NO\n"
            "CalculCPIV_SuiviCalcul : YES / NO\n"
            "CalculCPIV_VecX : Integer\n"
            "CalculCPIV_VecY : Integer\n"
        )

if __name__ == '__main__':
    sec = Security()
    print(sec.check_tiffile('test.tif'))
    print(sec.check_directory('/home/greg/Documents/MFEE/3A/BES_python/interface_CPIV'))
    print(sec.check_int('12.5'))
    print(sec.check_float('12.5'))
    print(sec.check_string(12.5))
    sec.ask_validation('This is a test message')
