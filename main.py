import frame_image
import frame_masque
from data_writer import data_file
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    parameters = data_file()
    parameters.read_pandas()    
    frame_image.FrameImageApp(root, parameters)
    root.mainloop()

    root = tk.Tk()
    frame_masque.FrameMasqueApp(root, parameters)
    parameters.write_file()
    root.mainloop()
