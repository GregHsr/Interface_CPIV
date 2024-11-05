import os
import tkinter as tk
from tkinter import filedialog, messagebox
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
        
    def ask_validdation(self, message):
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

if __name__ == '__main__':
    sec = Security()
    print(sec.check_tiffile('test.tif'))
    print(sec.check_directory('/home/greg/Documents/MFEE/3A/BES_python/interface_CPIV'))
    print(sec.check_int('12.5'))
    print(sec.check_float('12.5'))
    print(sec.check_string(12.5))
    sec.ask_validdation('This is a test message')
