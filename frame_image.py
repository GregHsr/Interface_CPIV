import tkinter as tk
from tkinter import filedialog, messagebox
from data_writer import data_file
from security import Security


class FrameImageApp(Security):
    def __init__(self, root, parameters):
        super().__init__()
        self.root = root
        self.root.title("File Selector")
        self.params = parameters

        self.selection = tk.StringVar(value="Choose an option")
        self.fileTWO1_path = tk.StringVar()
        self.fileTWO2_path = tk.StringVar()
        self.file_IMGdbl_path = tk.StringVar()
        self.seqdbl_dir_path = tk.StringVar()
        self.int_deb_value = tk.IntVar(value=0)
        self.int_inter_value = tk.IntVar(value=0)
        self.int_fin_value = tk.IntVar(value=0)
        self.seq_dir_path = tk.StringVar()

        self.options_typedata = ["TWO", "DBL", "SEQDBL", "SEQ"]

        self.create_widgets()

    def create_widgets(self):
        # Help button
        self.help_button = tk.Button(self.root, text="Help", command=self.show_help)
        self.help_button.grid(row=0, column=3, padx=10, pady=10)

        # Label for the dropdown
        tk.Label(self.root, text="Select Option:").grid(row=0,
                                                        column=0,
                                                        padx=10,
                                                        pady=10)

        # Dropdown menu
        tk.OptionMenu(self.root, self.selection,
                      *self.options_typedata,
                      command=self.update_widgets).grid(row=0,
                                                        column=1,
                                                        padx=10,
                                                        pady=10)

        # TWO selector
        # First file selector
        self.fileTWO1_label = tk.Label(self.root, text="Image 1:")
        self.fileTWO1_label.grid(row=1, column=0, padx=10, pady=10)
        self.fileTWO1_entry = tk.Entry(self.root,
                                       textvariable=self.fileTWO1_path,
                                       width=40)
        self.fileTWO1_entry.grid(row=1, column=1, padx=10, pady=10)
        self.fileTWO1_button = tk.Button(self.root,
                                         text="Browse",
                                         command=self.browse_fileTWO1)
        self.fileTWO1_button.grid(row=1, column=2, padx=10, pady=10)

        # Second file selector
        self.fileTWO2_label = tk.Label(self.root, text="Image 2:")
        self.fileTWO2_label.grid(row=2, column=0, padx=10, pady=10)
        self.fileTWO2_entry = tk.Entry(self.root,
                                       textvariable=self.fileTWO2_path,
                                       width=40)
        self.fileTWO2_entry.grid(row=2, column=1, padx=10, pady=10)
        self.fileTWO2_button = tk.Button(self.root,
                                         text="Browse",
                                         command=self.browse_fileTWO2)
        self.fileTWO2_button.grid(row=2, column=2, padx=10, pady=10)

        # DBL selector
        self.file_IMGdbl_label = tk.Label(self.root, text="Image double:")
        self.file_IMGdbl_label.grid(row=2, column=0, padx=10, pady=10)
        self.file_IMGdbl_entry = tk.Entry(self.root,
                                          textvariable=self.file_IMGdbl_path,
                                          width=40)
        self.file_IMGdbl_entry.grid(row=2, column=1, padx=10, pady=10)
        self.file_IMGdbl_button = tk.Button(self.root,
                                            text="Browse",
                                            command=self.browse_file_IMGdbl)
        self.file_IMGdbl_button.grid(row=2, column=2, padx=10, pady=10)

        # SEQDBL selector
        self.seqdbl_dir_label = tk.Label(self.root, text="Directory:")
        self.seqdbl_dir_label.grid(row=2, column=0, padx=10, pady=10)
        self.seqdbl_dir_entry = tk.Entry(self.root,
                                         textvariable=self.seqdbl_dir_path,
                                         width=40)
        self.seqdbl_dir_entry.grid(row=2, column=1, padx=10, pady=10)
        self.seqdbl_dir_button = tk.Button(self.root,
                                           text="Browse",
                                           command=self.browse_seqdbl_dir)
        self.seqdbl_dir_button.grid(row=2, column=2, padx=10, pady=10)

        # SEQ selector
        # Integer_debut input
        self.int_debut_label = tk.Label(self.root, text="Input_SEQdebut:")
        self.int_debut_entry = tk.Entry(self.root,
                                        textvariable=self.int_deb_value,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_debut_label.grid(row=1, column=0, padx=10, pady=10)
        self.int_debut_entry.grid(row=1, column=1, padx=10, pady=10)

        # Integer_inter input
        self.int_inter_label = tk.Label(self.root, text="Input_SEQinterImg:")
        self.int_inter_entry = tk.Entry(self.root,
                                        textvariable=self.int_inter_value,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_inter_label.grid(row=2, column=0, padx=10, pady=10)
        self.int_inter_entry.grid(row=2, column=1, padx=10, pady=10)

        # Integer_fin input
        self.int_fin_label = tk.Label(self.root, text="Input_SEQPaire:")
        self.int_fin_entry = tk.Entry(self.root,
                                      textvariable=self.int_fin_value,
                                      width=10,
                                      validate="key",
                                      validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_fin_label.grid(row=3, column=0, padx=10, pady=10)
        self.int_fin_entry.grid(row=3, column=1, padx=10, pady=10)

        # Dirname selector
        self.seq_dir_label = tk.Label(self.root, text="Directory:")
        self.seq_dir_entry = tk.Entry(self.root,
                                      textvariable=self.seq_dir_path,
                                      width=40)
        self.seq_dir_label.grid(row=4, column=0, padx=10, pady=10)
        self.seq_dir_button = tk.Button(self.root,
                                        text="Browse",
                                        command=self.browse_seq_dir)
        self.seq_dir_entry.grid(row=4, column=1, padx=10, pady=10)
        self.seq_dir_button.grid(row=4, column=2, padx=10, pady=10)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit).grid(row=5,
                                                                      column=1,
                                                                      padx=10,
                                                                      pady=10)

        #  Initialize
        self.update_widgets(self.selection.get())

    def update_widgets(self, selection):
        if selection == "Choose an option":
            # Hide all
            self.fileTWO1_label.grid_remove()
            self.fileTWO1_entry.grid_remove()
            self.fileTWO1_button.grid_remove()
            self.fileTWO2_label.grid_remove()
            self.fileTWO2_entry.grid_remove()
            self.fileTWO2_button.grid_remove()

            self.file_IMGdbl_label.grid_remove()
            self.file_IMGdbl_entry.grid_remove()
            self.file_IMGdbl_button.grid_remove()

            self.seqdbl_dir_label.grid_remove()
            self.seqdbl_dir_entry.grid_remove()
            self.seqdbl_dir_button.grid_remove()

            self.int_debut_label.grid_remove()
            self.int_debut_entry.grid_remove()
            self.int_inter_label.grid_remove()
            self.int_inter_entry.grid_remove()
            self.int_fin_label.grid_remove()
            self.int_fin_entry.grid_remove()
            self.seq_dir_label.grid_remove()
            self.seq_dir_entry.grid_remove()
            self.seq_dir_button.grid_remove()

        elif selection == "TWO":
            # Show file 1, hide file 2 and integer input
            self.fileTWO1_label.grid()
            self.fileTWO1_entry.grid()
            self.fileTWO1_button.grid()
            self.fileTWO2_label.grid()
            self.fileTWO2_entry.grid()
            self.fileTWO2_button.grid()

            self.file_IMGdbl_label.grid_remove()
            self.file_IMGdbl_entry.grid_remove()
            self.file_IMGdbl_button.grid_remove()

            self.seqdbl_dir_label.grid_remove()
            self.seqdbl_dir_entry.grid_remove()
            self.seqdbl_dir_button.grid_remove()

            self.int_debut_label.grid_remove()
            self.int_debut_entry.grid_remove()
            self.int_inter_label.grid_remove()
            self.int_inter_entry.grid_remove()
            self.int_fin_label.grid_remove()
            self.int_fin_entry.grid_remove()
            self.seq_dir_label.grid_remove()
            self.seq_dir_entry.grid_remove()
            self.seq_dir_button.grid_remove()

        elif selection == "DBL":
            # Show file 2, hide file 1 and integer input
            self.fileTWO1_label.grid_remove()
            self.fileTWO1_entry.grid_remove()
            self.fileTWO1_button.grid_remove()
            self.fileTWO2_label.grid_remove()
            self.fileTWO2_entry.grid_remove()
            self.fileTWO2_button.grid_remove()

            self.file_IMGdbl_label.grid()
            self.file_IMGdbl_entry.grid()
            self.file_IMGdbl_button.grid()

            self.seqdbl_dir_label.grid_remove()
            self.seqdbl_dir_entry.grid_remove()
            self.seqdbl_dir_button.grid_remove()

            self.int_debut_label.grid_remove()
            self.int_debut_entry.grid_remove()
            self.int_inter_label.grid_remove()
            self.int_inter_entry.grid_remove()
            self.int_fin_label.grid_remove()
            self.int_fin_entry.grid_remove()
            self.seq_dir_label.grid_remove()
            self.seq_dir_entry.grid_remove()
            self.seq_dir_button.grid_remove()

        elif selection == "SEQDBL":
            self.fileTWO1_label.grid_remove()
            self.fileTWO1_entry.grid_remove()
            self.fileTWO1_button.grid_remove()
            self.fileTWO2_label.grid_remove()
            self.fileTWO2_entry.grid_remove()
            self.fileTWO2_button.grid_remove()

            self.file_IMGdbl_label.grid_remove()
            self.file_IMGdbl_entry.grid_remove()
            self.file_IMGdbl_button.grid_remove()

            self.seqdbl_dir_label.grid()
            self.seqdbl_dir_entry.grid()
            self.seqdbl_dir_button.grid()

            self.int_debut_label.grid_remove()
            self.int_debut_entry.grid_remove()
            self.int_inter_label.grid_remove()
            self.int_inter_entry.grid_remove()
            self.int_fin_label.grid_remove()
            self.int_fin_entry.grid_remove()
            self.seq_dir_label.grid_remove()
            self.seq_dir_entry.grid_remove()
            self.seq_dir_button.grid_remove()

        else:
            # Show integer input, hide file selectors
            self.fileTWO1_label.grid_remove()
            self.fileTWO1_entry.grid_remove()
            self.fileTWO1_button.grid_remove()
            self.fileTWO2_label.grid_remove()
            self.fileTWO2_entry.grid_remove()
            self.fileTWO2_button.grid_remove()

            self.file_IMGdbl_label.grid_remove()
            self.file_IMGdbl_entry.grid_remove()
            self.file_IMGdbl_button.grid_remove()

            self.seqdbl_dir_label.grid_remove()
            self.seqdbl_dir_entry.grid_remove()
            self.seqdbl_dir_button.grid_remove()

            self.int_debut_label.grid()
            self.int_debut_entry.grid()
            self.int_inter_label.grid()
            self.int_inter_entry.grid()
            self.int_fin_label.grid()
            self.int_fin_entry.grid()
            self.seq_dir_label.grid()
            self.seq_dir_entry.grid()
            self.seq_dir_button.grid()

    def browse_fileTWO1(self):
        file_path = filedialog.askopenfilename(title="Select File 1",
                                               filetypes=[("Image Files","*.tif")])
        if file_path:
            self.fileTWO1_path.set(file_path)

    def browse_fileTWO2(self):
        file_path = filedialog.askopenfilename(title="Select File 2",
                                               filetypes=[("Image Files","*.tif")])
        if file_path:
            self.fileTWO2_path.set(file_path)

    def browse_file_IMGdbl(self):
        file_path = filedialog.askopenfilename(title="Select File 2",
                                               filetypes=[("Image Files","*.tif")])
        if file_path:
            self.file_IMGdbl_path.set(file_path)

    def browse_seqdbl_dir(self):
        dir_path = filedialog.askdirectory(title="Select Directory")
        if dir_path:
            self.seqdbl_dir_path.set(dir_path)

    def browse_seq_dir(self):
        dir_path = filedialog.askdirectory(title="Select Directory")
        if dir_path:
            self.seq_dir_path.set(dir_path)

    def submit(self):
        selection = self.selection.get()

        if selection == "Choose an option":
            messagebox.showerror("Please select an option.")
            return

        elif selection == "TWO":
            fileTWO1 = self.fileTWO1_path.get()
            fileTWO2 = self.fileTWO2_path.get()
            if not fileTWO1:
                messagebox.showerror("Error", "Please select TIF image for file 1.")
                return
            if not fileTWO2:
                messagebox.showerror("Error", "Please select TIF image for file 2.")
                return
            if Security.check_tiffile(self, fileTWO1)==False:
                messagebox.showerror("Error", "Please select a valid TIF image for file 1.")
                return
            if Security.check_tiffile(self, fileTWO2)==False:
                messagebox.showerror("Error", "Please select a valid TIF image for file 2.")
                return
            state = "Submission Successful"
            self.params.change_variable('Input_ImgTWO1', fileTWO1)
            self.params.change_variable('Input_ImgTWO2', fileTWO2)
            self.params.change_variable('Input_typedata', 'TWO')
            messagebox.showinfo("Info",state)

        elif selection == "DBL":
            file_IMGdbl = self.file_IMGdbl_path.get()
            if not file_IMGdbl:
                messagebox.showerror("Error", "Please select a TIF image.")
                return
            if Security.check_tiffile(self, file_IMGdbl)==False:
                messagebox.showerror("Error", "Please select a valid TIF image.")
                return
            self.params.change_variable('Input_Imgdouble', file_IMGdbl)
            messagebox.showinfo("Submission Successful",
                                f"Option: {selection}\nFile 2: {file_IMGdbl}")
            self.params.change_variable('Input_Imgdouble', file_IMGdbl)
            self.params.change_variable('Input_typedata', 'DBL')

        elif selection == "SEQDBL":
            seqdbl_dir = self.seqdbl_dir_path.get()
            if not seqdbl_dir:
                messagebox.showerror("Error", "Please select Directory.")
                return
            if Security.check_directory(self, seqdbl_dir)==False:
                messagebox.showerror("Error", "Please select a valid Directory.")
                return
            messagebox.showinfo("Submission Successful",
                                f"Option: {selection}\nDir: {seqdbl_dir}")
            self.params.change_variable('Input_SEQDirname', seqdbl_dir)
            self.params.change_variable('Input_typedata', 'SEQDBL')

        else:
            try:
                int_deb_value = self.int_deb_value.get()
                int_inter_value = self.int_inter_value.get()
                int_fin_value = self.int_fin_value.get()
                print(int_deb_value, int_inter_value, int_fin_value)
            except:
                messagebox.showerror("Error", "Please enter valid integers.")
                return
            
            seq_dir = self.seq_dir_path.get()

            if not seq_dir:
                messagebox.showerror("Error", "Please select Directory.")
                return
            if Security.check_directory(self, seq_dir)==False:
                messagebox.showerror("Error", "Please select a valid Directory.")
                return
            for k in [int_deb_value, int_inter_value, int_fin_value]:
                if Security.check_int(self, k)==False:
                    messagebox.showerror("Error", f"Please enter valid integers for {k}.")
                    return
            
            self.params.change_variable('Input_SEQdebut', int_deb_value)
            self.params.change_variable('Input_SEQinterImg', int_inter_value)
            self.params.change_variable('Input_SEQinterPaire', int_fin_value)
            self.params.change_variable('Input_SEQDirname', seq_dir)
            self.params.change_variable('Input_typedata', 'SEQ')
            messagebox.showinfo("Submission Successful",
                                f"Option: {selection}\n" + 
                                f"Int: {int_deb_value}\n" +
                                f"Int: {int_inter_value}\n" +
                                f"Int: {int_fin_value}\n" +
                                f"Dir: {seq_dir}")

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    parameters = data_file()
    parameters.read_pandas()
    app = FrameImageApp(root, parameters)
    root.mainloop()
    parameters.write_file()
