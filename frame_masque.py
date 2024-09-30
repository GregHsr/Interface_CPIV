import tkinter as tk
from tkinter import filedialog, messagebox
from data_writer import data_file


class FrameImageApp:
    def __init__(self, root, parameters):
        self.root = root
        self.root.title("File Selector")

        self.selection = tk.StringVar(value="Choose an option")
        self.fileTWO1_path = tk.StringVar()
        self.fileTWO2_path = tk.StringVar()
        self.file_IMGdbl_path = tk.StringVar()
        self.seqdbl_dir_path = tk.StringVar()
        self.integer_value = tk.IntVar(value=0)

        self.options_typedata = ["TWO", "DBL", "SEQDBL", "SEQ"]

        self.create_widgets()

    def create_widgets(self):
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
        self.fileTWO1_label = tk.Label(self.root, text="File 1:")
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
        self.fileTWO2_label = tk.Label(self.root, text="File 2:")
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
        self.file_IMGdbl_label = tk.Label(self.root, text="File 2:")
        self.file_IMGdbl_label.grid(row=2, column=0, padx=10, pady=10)
        self.file_IMGdbl_entry = tk.Entry(self.root,
                                          textvariable=self.file_IMGdbl_path,
                                          width=40)
        self.file_IMGdbl_entry.grid(row=2, column=1, padx=10, pady=10)
        self.file_IMGdbl_button = tk.Button(self.root,
                                            text="Browse",
                                            command=self.browse_file_IMGdbl)
        self.file_IMGdbl_button.grid(row=2, column=2, padx=10, pady=10)

        # Integer input
        self.int_label = tk.Label(self.root, text="Enter an Integer:")
        self.int_entry = tk.Entry(self.root,
                                  textvariable=self.integer_value,
                                  width=10)
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

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit).grid(row=3,
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

            self.int_label.grid_remove()
            self.int_entry.grid_remove()

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

            self.int_label.grid_remove()
            self.int_entry.grid_remove()

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

            self.int_label.grid_remove()
            self.int_entry.grid_remove()

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

            self.int_label.grid_remove()
            self.int_entry.grid_remove()

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

            self.int_label.grid(row=1, column=0, padx=10, pady=10)
            self.int_entry.grid(row=1, column=1, padx=10, pady=10)

    def browse_fileTWO1(self):
        file_path = filedialog.askopenfilename(title="Select File 1")
        if file_path:
            self.fileTWO1_path.set(file_path)

    def browse_fileTWO2(self):
        file_path = filedialog.askopenfilename(title="Select File 2")
        if file_path:
            self.fileTWO2_path.set(file_path)

    def browse_file_IMGdbl(self):
        file_path = filedialog.askopenfilename(title="Select File 2")
        if file_path:
            self.file_IMGdbl_path.set(file_path)

    def browse_seqdbl_dir(self):
        dir_path = filedialog.askdirectory(title="Select Directory")
        if dir_path:
            self.seqdbl_dir_path.set(dir_path)

    def submit(self):
        selection = self.selection.get()

        if selection == "Choose an option":
            messagebox.showerror("Please select an option.")
            return

        elif selection == "TWO":
            fileTWO1 = self.fileTWO1_path.get()
            fileTWO2 = self.fileTWO2_path.get()
            if not fileTWO1:
                messagebox.showerror("Error", "Please select File 1.")
                return
            if not fileTWO2:
                messagebox.showerror("Error", "Please select File 2.")
                return
            state = "Submission Successful"
            parameters.change_variable('Input_ImgTWO1', fileTWO1)
            parameters.change_variable('Input_ImgTWO2', fileTWO2)
            parameters.change_variable('Input_typedata', 'TWO')
            messagebox.showinfo(state)

        elif selection == "DBL":
            file_IMGdbl = self.file_IMGdbl_path.get()
            if not file_IMGdbl:
                messagebox.showerror("Error", "Please select File 2.")
                return
            parameters.change_variable('Input_Imgdouble', file_IMGdbl)
            messagebox.showinfo("Submission Successful",
                                f"Option: {selection}\nFile 2: {file_IMGdbl}")
            parameters.change_variable('Input_Imgdouble', file_IMGdbl)
            parameters.change_variable('Input_typedata', 'DBL')

        elif selection == "SEQDBL":
            seqdbl_dir = self.seqdbl_dir_path.get()
            if not seqdbl_dir:
                messagebox.showerror("Error", "Please select Directory.")
                return
            messagebox.showinfo("Submission Successful",
                                f"Option: {selection}\nDir: {seqdbl_dir}")
            parameters.change_variable('Input_SEQDirname', seqdbl_dir)
            parameters.change_variable('Input_typedata', 'SEQDBL')
        else:
            int_value = self.integer_value.get()
            messagebox.showinfo("Submission Successful",
                                f"Option: {selection}\nInteger: {int_value}")

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    parameters = data_file()
    parameters.read_pandas()
    app = FrameImageApp(root, parameters)
    root.mainloop()
    parameters.write_file()
