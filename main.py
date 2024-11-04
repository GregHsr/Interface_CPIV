import frame_image
import frame_masque
import frame_calcul
from data_writer import data_file
import tkinter as tk

if __name__ == "__main__":
    parameters = data_file()
    parameters.read_pandas()   

    root = tk.Tk()
    frame_image.FrameImageApp(root, parameters)
    root.mainloop()

    root = tk.Tk()
    frame_masque.FrameMasqueApp(root, parameters)
    root.mainloop()

    root = tk.Tk()
    frame_calcul.FrameCalculApp(root, parameters)
    root.mainloop()

    parameters.write_file()
