import tkinter as tk
from tkinter import filedialog, messagebox
from data_writer import data_file
from security import Security


class FrameCalculApp(Security):
    def __init__(self, root, parameters):
        super().__init__()
        self.root = root
        self.root.title("File Selector")
        self.params = parameters

        self.type_meth_selection = tk.StringVar(value="Choose an option")
        self.bool_ROI_selection = tk.StringVar(value="Choose an option")
        self.int_dimx = tk.IntVar(value=0)
        self.int_dimy = tk.IntVar(value=0)
        self.float_recouvrx = tk.DoubleVar(value=0.0)
        self.float_recouvry = tk.DoubleVar(value=0.0)
        self.int_roix1 = tk.IntVar(value=0)
        self.int_roiy1 = tk.IntVar(value=0)
        self.int_roix2 = tk.IntVar(value=0)
        self.int_roiy2 = tk.IntVar(value=0)
        self.outil_conv = tk.StringVar(value="Choose an option")
        self.filtre_postcalc = tk.StringVar(value="Choose an option")
        self.bool_suivi_calc = tk.StringVar(value="Choose an option")
        self.vecx = tk.IntVar(value=0)
        self.vecy = tk.IntVar(value=0)

        self.type_meth = ["PIVDEFORM", "PIVDECAL", "PIVSIMPLE"]
        self.bool_ROI = ["YES", "NO"]
        self.bool_outconv = ["YES", "NO"]
        self.bool_postcalc = ["YES", "NO"]
        self.bool_l_suivicalc = ["YES", "NO"]

        self.create_widgets()

    def create_widgets(self):
        # Help button
        self.help_button = tk.Button(self.root, text="Help", command=self.show_help)
        self.help_button.grid(row=0, column=3, padx=10, pady=10)

        # Dropdown
        self.firstmenu_label = tk.Label(self.root, text="Method Type:").grid(row=0,
                                                                             column=0,
                                                                             padx=10,
                                                                             pady=10)
        self.firstmenu = tk.OptionMenu(self.root, self.type_meth_selection,
                                       *self.type_meth,
                                       command=self.update_widgets).grid(row=0,
                                                                         column=1,
                                                                         padx=10,
                                                                         pady=10)

        # Integer X input
        self.int_xinput_label = tk.Label(self.root, text="Dim X:")
        self.int_xinput_entry = tk.Entry(self.root,
                                        textvariable=self.int_dimx,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_xinput_label.grid(row=1, column=0, padx=10, pady=10)
        self.int_xinput_entry.grid(row=1, column=1, padx=10, pady=10)

        # Integer Y input
        self.int_yinput_label = tk.Label(self.root, text="Dim Y:")
        self.int_yinput_entry = tk.Entry(self.root,
                                        textvariable=self.int_dimy,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_yinput_label.grid(row=1, column=2, padx=10, pady=10)
        self.int_yinput_entry.grid(row=1, column=3, padx=10, pady=10)

        # Float recouvrement input
        self.floatx_label = tk.Label(self.root, text="Recouvrement:")
        self.floatx_entry = tk.Entry(self.root,
                                    textvariable=self.float_recouvrx,
                                    width=10,
                                    validate="key",
                                    validatecommand=(self.root.register(self.validate_float), '%P'))
        self.floatx_label.grid(row=2, column=0, padx=10, pady=10)
        self.floatx_entry.grid(row=2, column=1, padx=10, pady=10)
        self.floaty_entry = tk.Entry(self.root,
                                     textvariable=self.float_recouvry,
                                     width=10,
                                     validate="key",
                                     validatecommand=(self.root.register(self.validate_float), '%P'))
        self.floaty_entry.grid(row=2, column=3, padx=10, pady=10)

        # Dropdown
        self.menu_ROI_label = tk.Label(self.root,
                                       text="Region of interest:").grid(row=3,
                                                                        column=0,
                                                                        padx=10,
                                                                        pady=10)
        self.menu_ROI = tk.OptionMenu(self.root, self.bool_ROI_selection,
                                       *self.bool_ROI,
                                       command=self.update_widgets).grid(row=3,
                                                                         column=1,
                                                                         padx=10,
                                                                         pady=10)

        # Integer X1 ROI input
        self.int_x1roi_label = tk.Label(self.root, text="X1:")
        self.int_x1roi_entry = tk.Entry(self.root,
                                        textvariable=self.int_roix1,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_x1roi_label.grid(row=4, column=0, padx=10, pady=10)
        self.int_x1roi_entry.grid(row=4, column=1, padx=10, pady=10)

        # Integer X2 ROI input
        self.int_x2roi_label = tk.Label(self.root, text="X2:")
        self.int_x2roi_entry = tk.Entry(self.root,
                                        textvariable=self.int_roix2,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_x2roi_label.grid(row=4, column=2, padx=10, pady=10)
        self.int_x2roi_entry.grid(row=4, column=3, padx=10, pady=10)

        # Integer Y1 ROI input
        self.int_y1roi_label = tk.Label(self.root, text="Y1:")
        self.int_y1roi_entry = tk.Entry(self.root,
                                        textvariable=self.int_roiy1,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_y1roi_label.grid(row=5, column=0, padx=10, pady=10)
        self.int_y1roi_entry.grid(row=5, column=1, padx=10, pady=10)

        # Integer Y2 ROI input
        self.int_y2roi_label = tk.Label(self.root, text="Y2:")
        self.int_y2roi_entry = tk.Entry(self.root,
                                        textvariable=self.int_roiy2,
                                        width=10,
                                        validate="key",
                                        validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_y2roi_label.grid(row=5, column=2, padx=10, pady=10)
        self.int_y2roi_entry.grid(row=5, column=3, padx=10, pady=10)

        # Dropdown outil conv
        self.menu_outilconv_label = tk.Label(self.root,
                                             text="Outil de convergence:").grid(row=6,
                                                                              column=0,
                                                                              padx=10,
                                                                              pady=10)
        self.menu_outilconv = tk.OptionMenu(self.root, self.outil_conv,
                                            *self.bool_outconv,
                                            command=self.update_widgets).grid(row=6,
                                                                              column=1,
                                                                              padx=10,
                                                                              pady=10)

        # Dropdown filtre postcalc
        self.menu_filtrepostcalc_label = tk.Label(self.root,
                                                  text="Filtre post-calcul:").grid(row=7,
                                                                                  column=0,
                                                                                  padx=10,
                                                                                  pady=10)
        self.menu_filtrepostcalc = tk.OptionMenu(self.root, self.filtre_postcalc,
                                                    *self.bool_postcalc,
                                                    command=self.update_widgets).grid(row=7,
                                                                                    column=1,
                                                                                    padx=10,
                                                                                    pady=10)

        # Dropdown suivi calc
        self.menu_suivicalc_label = tk.Label(self.root,
                                             text="Suivi calcul:").grid(row=8,
                                                                       column=0,
                                                                       padx=10,
                                                                       pady=10)
        self.menu_suivicalc = tk.OptionMenu(self.root, self.bool_suivi_calc,
                                            *self.bool_l_suivicalc,
                                            command=self.update_widgets).grid(row=8,
                                                                              column=1,
                                                                              padx=10,
                                                                              pady=10)

        # Integer vector input
        self.int_vecx_label = tk.Label(self.root, text="Vecteur X:")
        self.int_vecx_entry = tk.Entry(self.root,
                                       textvariable=self.vecx,
                                       width=10,
                                       validate="key",
                                       validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_vecx_label.grid(row=9, column=0, padx=10, pady=10)
        self.int_vecx_entry.grid(row=9, column=1, padx=10, pady=10)
        self.int_vecy_label = tk.Label(self.root, text="Vecteur Y:")
        self.int_vecy_entry = tk.Entry(self.root,
                                       textvariable=self.vecy,
                                       width=10,
                                       validate="key",
                                       validatecommand=(self.root.register(self.validate_int), '%P'))
        self.int_vecy_label.grid(row=9, column=2, padx=10, pady=10)
        self.int_vecy_entry.grid(row=9, column=3, padx=10, pady=10)

        # Submit button
        tk.Button(self.root, text="Submit", command=self.submit).grid(row=10,
                                                                      column=1,
                                                                      padx=10,
                                                                      pady=10)

        #  Initialize
        self.update_widgets(self.type_meth_selection.get())

    def update_zonecalcul(self, state):
        if state == "hide":
            # Hide ROI int
            self.int_x1roi_label.grid_remove()
            self.int_x1roi_entry.grid_remove()
            self.int_x2roi_label.grid_remove()
            self.int_x2roi_entry.grid_remove()
            self.int_y1roi_label.grid_remove()
            self.int_y1roi_entry.grid_remove()
            self.int_y2roi_label.grid_remove()
            self.int_y2roi_entry.grid_remove()

        else:
            self.int_x1roi_label.grid()
            self.int_x1roi_entry.grid()
            self.int_x2roi_label.grid()
            self.int_x2roi_entry.grid()
            self.int_y1roi_label.grid()
            self.int_y1roi_entry.grid()
            self.int_y2roi_label.grid()
            self.int_y2roi_entry.grid()

    def update_suivicalc(self, state):
        if state == "hide":
            self.int_vecx_label.grid_remove()
            self.int_vecx_entry.grid_remove()
            self.int_vecy_label.grid_remove()
            self.int_vecy_entry.grid_remove()

        else:
            self.int_vecx_label.grid()
            self.int_vecx_entry.grid()
            self.int_vecy_label.grid()
            self.int_vecy_entry.grid()

    def update_widgets(self,selection):
        suivicalc = self.bool_suivi_calc.get()
        sel_zone = self.bool_ROI_selection.get()
        if sel_zone == "Choose an option":
            self.update_zonecalcul("hide")
        if suivicalc == "Choose an option":
            self.update_suivicalc("hide")
        if sel_zone == "YES":
            self.update_zonecalcul("show")
        elif sel_zone == "NO":
            self.update_zonecalcul("hide")
        if suivicalc == "YES":
            self.update_suivicalc("show")
        elif suivicalc == "NO":
            self.update_suivicalc("hide")


    def submit(self):
        if self.type_meth_selection.get() == "Choose an option":
            messagebox.showerror("Error", "Please select a method type")
            return
        if self.bool_ROI_selection.get() == "YES":
            if self.int_roix1.get() == 0 or self.int_roix2.get() == 0 or self.int_roiy1.get() == 0 or self.int_roiy2.get() == 0:
                messagebox.showerror("Error", "Please enter the ROI values")
                return
        else :
            self.params.change_variable('CalculCPIV_meths', self.type_meth_selection.get())

        dimX = self.int_dimx.get()
        dimY = self.int_dimy.get()
        if dimX == 0 or dimY == 0:
            messagebox.showerror("Error", "Please enter the dimensions")
            return
        else:
            self.params.change_variable('CalculCPIV_dimXYcell', f'{dimX} {dimY}')

        recouvrx = self.float_recouvrx.get()
        recouvry = self.float_recouvry.get()
        if recouvrx == 0. and recouvry == 0.:
            proceed = self.ask_validation("Recouvrement values are still at 0, is this what you want?")
            if proceed == False:
                return
            else:
                self.params.change_variable('CalculCPIV_recouv', f'{recouvrx} {recouvry}')
        elif recouvrx >= 1. or recouvry == 1.:
            messagebox.showerror("Error", "Recouvrement values must be less than 1")
            return
        else:
            self.params.change_variable('CalculCPIV_recouv', f'{recouvrx} {recouvry}')

        if self.bool_ROI_selection.get() == "Choose an option":
            messagebox.showerror("Error", "Please select an option for the ROI")
            return
        else:
            if self.bool_ROI_selection.get() == "YES":
                roix1 = self.int_roix1.get()
                roix2 = self.int_roix2.get()
                roiy1 = self.int_roiy1.get()
                roiy2 = self.int_roiy2.get()
                if roix1 == 0 or roix2 == 0 or roiy1 == 0 or roiy2 == 0:
                    messagebox.showerror("Error", "Please enter the ROI values")
                    return
                else:
                    self.params.change_variable('CalculCPIV_ROIval', f'{roix1} {roix2} {roiy1} {roiy2}')
            self.params.change_variable('CalculCPIV_ROI', self.bool_ROI_selection.get())

        if self.outil_conv.get() == "Choose an option":
            messagebox.showerror("Error", "Please select an option for the outil de convergence")
            return
        else:
            self.params.change_variable('CalculCPIV_ConvTools', self.outil_conv.get())

        if self.filtre_postcalc.get() == "Choose an option":
            messagebox.showerror("Error", "Please select an option for the filtre post-calcul")
            return
        else:
            self.params.change_variable('CalculCPIV_FiltrePostCalcul', self.filtre_postcalc.get())

        if self.bool_suivi_calc.get() == "Choose an option":
            messagebox.showerror("Error", "Please select an option for the suivi calcul")
            return
        else:
            if self.bool_suivi_calc.get() == "YES":
                vec_x = self.vecx.get()
                vec_y = self.vecy.get()
                if vec_x == 0 or vec_y == 0:
                    messagebox.showerror("Error", "Please enter the vector values")
                    return
                else:
                    self.params.change_variable('CalculCPIV_VecX', str(vec_x))
                    self.params.change_variable('CalculCPIV_VecY', str(vec_y))
            self.params.change_variable('CalculCPIV_SuiviCalcul', self.bool_suivi_calc.get())

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    parameters = data_file()
    parameters.read_pandas()
    app = FrameCalculApp(root, parameters)
    root.mainloop()
    parameters.write_file()
