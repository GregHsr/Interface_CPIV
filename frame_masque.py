import tkinter as tk
from tkinter import filedialog, messagebox
from data_writer import data_file
from security import Security

class FrameMasqueApp(Security):
    def __init__(self, root, parameters):
        super().__init__()
        self.root = root
        self.root.title("File Selector")
        self.params = parameters

        self.bool_selection = tk.StringVar(value="Choose an option")
        self.typemenu_selection = tk.StringVar(value="Choose an option")
        self.file_One_path = tk.StringVar()
        self.file_Seq_path = tk.StringVar()

        self.options_mask = ["YES", "NO"]
        self.type_mask = ["ONE","SEQ"]

        self.create_widgets()

    def create_widgets(self):
        # Help button
        self.help_button = tk.Button(self.root, text="Help", command=self.show_help)
        self.help_button.grid(row=0, column=3, padx=10, pady=10)
        
        # Dropdown
        self.firstmenu_label = tk.Label(self.root, text="Mask:").grid(row=0,
                                                                      column=0,
                                                                      padx=10,
                                                                      pady=10)
        self.firstmenu = tk.OptionMenu(self.root, self.bool_selection,
                                       *self.options_mask,
                                       command=self.update_widgets).grid(row=0,
                                                                         column=1,
                                                                         padx=10,
                                                                         pady=10)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit).grid(row=3,
                                                                      column=1,
                                                                      padx=10,
                                                                      pady=10)

        # Type Menu
        self.typemenu_label = tk.Label(self.root, text="Type:")
        self.typemenu_label.grid(row=1, column=0, padx=10, pady=10)
        self.typemenu_menu = tk.OptionMenu(self.root, self.typemenu_selection,
                                            *self.type_mask,
                                            command=self.update_widget_type)
        self.typemenu_menu.grid(row=1, column=1, padx=10, pady=10)

        # One selector
        self.file_One_label = tk.Label(self.root, text="Image:")
        self.file_One_label.grid(row=2, column=0, padx=10, pady=10)
        self.file_One_entry = tk.Entry(self.root,
                                       textvariable=self.file_One_path,
                                       width=40)
        self.file_One_entry.grid(row=2, column=1, padx=10, pady=10)
        self.file_One_button = tk.Button(self.root,
                                         text="Browse",
                                         command=self.browse_file_One)
        self.file_One_button.grid(row=2, column=2, padx=10, pady=10)

        # Seq selector
        self.file_Seq_label = tk.Label(self.root, text="Seq directory:")
        self.file_Seq_label.grid(row=2, column=0, padx=10, pady=10)
        self.file_Seq_entry = tk.Entry(self.root,
                                       textvariable=self.file_Seq_path,
                                       width=40)
        self.file_Seq_entry.grid(row=2, column=1, padx=10, pady=10)
        self.file_Seq_button = tk.Button(self.root,
                                         text="Browse",
                                         command=self.browse_file_Seq)  
        self.file_Seq_button.grid(row=2, column=2, padx=10, pady=10)

        #  Initialize
        self.update_widgets(self.bool_selection.get())
        self.update_widget_type(self.typemenu_selection.get())

    def update_typemenu(self, state):
        if state == "hide":
            self.typemenu_label.grid_remove()
            self.typemenu_menu.grid_remove()
        else:
            self.typemenu_label.grid()
            self.typemenu_menu.grid()

    def update_file_One(self, state):
        if state == "hide":
            self.file_One_label.grid_remove()
            self.file_One_entry.grid_remove()
            self.file_One_button.grid_remove()
        else:
            self.file_One_label.grid()
            self.file_One_entry.grid()
            self.file_One_button.grid()

    def update_file_Seq(self, state):
        if state == "hide":
            self.file_Seq_label.grid_remove()
            self.file_Seq_entry.grid_remove()
            self.file_Seq_button.grid_remove()
        else:
            self.file_Seq_label.grid()
            self.file_Seq_entry.grid()
            self.file_Seq_button.grid()

    def browse_file_One(self):
        file_path = filedialog.askopenfilename(title="Select File",
                                               filetypes=[("Image Files","*.tif")])
        if file_path:
            self.file_One_path.set(file_path)

    def browse_file_Seq(self):
        file_path = filedialog.askdirectory(title="Select Directory")
        if file_path:
            self.file_Seq_path.set(file_path)

    def update_widgets(self, selection):
        if selection == "Choose an option":
            self.update_typemenu("hide")
            self.update_file_One("hide")
            self.update_file_Seq("hide")

        elif selection == "YES":
            self.update_typemenu("show")
            
        elif selection == "NO":
            self.update_typemenu("hide")
            self.update_file_One("hide")
            self.update_file_Seq("hide")

        else:
            self.update_typemenu("hide")
            self.update_file_One("hide")
            self.update_file_Seq("hide")

    def update_widget_type(self, selection):
        if selection == "ONE":
            self.update_file_One("show")
            self.update_file_Seq("hide")

        elif selection == "SEQ":
            self.update_file_One("hide")
            self.update_file_Seq("show")

        else:
            self.update_file_One("hide")
            self.update_file_Seq("hide")

    def submit(self):
        selection = self.bool_selection.get()
        if selection == "Choose an option":
            messagebox.showerror("Error","Please select an option.")
            return

        elif selection == "NO":
            bool_sel = self.bool_selection.get()
            if not bool_sel:
                messagebox.showerror("Error", "Please select an option.")
                return
            state = "Submission Successful"
            self.params.change_variable('Input_Masque', 'NO')
            messagebox.showinfo(state, "No Mask selected")

        elif selection == "YES":
            bool_sel = self.bool_selection.get()
            one_path = self.file_One_path.get()
            seq_path = self.file_Seq_path.get()

            if not seq_path and not one_path:
                messagebox.showerror("Error", "Please select an option.")
                return
            elif not seq_path:
                if Security.check_tiffile(self, one_path) == False:
                    messagebox.showerror("Error", "Please select a valid TIF image.")
                    return
                self.params.change_variable('Input_TypeMasque', 'ONE')
                self.params.change_variable('Input_Masque', 'OK')
                self.params.change_variable('Input_OneNameMasque', one_path)
            elif not one_path:
                if Security.check_directory(self, seq_path) == False:
                    messagebox.showerror("Error", "Please select a valid directory.")
                    return
                self.params.change_variable('Input_TypeMasque', 'SEQ')
                self.params.change_variable('Input_Masque', 'OK')
                self.params.change_variable('Input_SeqDirMasque', seq_path)
            else:
                messagebox.showerror("Error","An unknown error occured, please reload")
                return
            messagebox.showinfo("Submission Successful", "Mask selected")

        else:
            messagebox.showerror("Error","An unknown error occured, please reload")
            return

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    parameters = data_file()
    parameters.read_pandas()
    app = FrameMasqueApp(root, parameters)
    root.mainloop()
    parameters.write_file()
