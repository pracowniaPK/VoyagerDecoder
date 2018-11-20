from sys import exit
from functools import partial

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from scipy.io import wavfile

class Application(tk.Frame):
    def __init__(self, master, path):
        self.rate, data = wavfile.read(path)
        self.datal = [s[0] for s in data]
        self.create_widgets()

        f, self.a = plt.subplots()
        self.canvas = FigureCanvasTkAgg(f, master=master)
        self.canvas.get_tk_widget().grid(column=1, row=1, columnspan=2)
        self.minor_custom_offset = 0
        self.major_custom_offset = 0
        self.plot()

    def create_widgets(self):
        label1 = tk.Label(root, text="przesunięcie poziome", font=(16))
        label1.grid(column=1, row=2, columnspan=2, 
            sticky=(tk.W, tk.N), pady=(12, 0))
        self.slider_offset = tk.Scale(root, from_=0, to=1700, 
            orient=tk.HORIZONTAL, command=self.update_plot)
        self.slider_offset.grid(column=1, row=3, columnspan=2, 
            sticky=(tk.W, tk.E))
        self.slider_offset.set(0)

        label2 = tk.Label(root, text="przesunięcie pionowe", font=(16))
        label2.grid(column=1, row=4, columnspan=2, sticky=(tk.W), 
            pady=(12, 0))
        self.slider_initial = tk.Scale(root, from_=0, to=512, 
            orient=tk.HORIZONTAL, command=self.update_plot)
        self.slider_initial.grid(column=1, row=5, columnspan=2, 
            sticky=(tk.W, tk.E))

        button_update = tk.Button(root, text="aktualizuj", 
            command=self.update_plot)
        button_update.grid(column=1, row=6)
        button_close = tk.Button(root, text="zamknij", command=exit)
        button_close.grid(column=2, row=6)

    def update_plot(self, *args):
        self.major_custom_offset = self.slider_offset.get()
        self.minor_custom_offset = self.slider_initial.get()
        self.plot()

    def plot(self):
        width = 734.4
        initial_offset = int((31.3363)*self.rate) + self.minor_custom_offset
        img = [[] for _ in range(int(width))]
        for i in range(self.major_custom_offset, 512+self.major_custom_offset):
            line_offset = initial_offset + int(i*width)
            for j in range(int(width)):
                img[j].append(self.datal[line_offset + j])

        self.a.imshow(img, cmap=plt.get_cmap("Greys"), aspect=0.59)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("voyager decoder")
    app = Application(root, "voy.wav")
    root.mainloop()
    root.destroy()
