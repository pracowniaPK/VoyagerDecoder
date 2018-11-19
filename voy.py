from sys import exit
from functools import partial

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from scipy.io import wavfile

class Application(tk.Frame):
    def __init__(self, master, path):
        tk.Frame.__init__(self, master)
        self.rate, data = wavfile.read(path)
        self.datal = [s[0] for s in data]
        self.datar = [s[1] for s in data]
        self.custom_offset = 0
        self.initial_custom_offset = 0
        self.drawing = None
        self.create_widgets()

    def create_widgets(self):
        self.plot()
        label1 = tk.Label(root, text="przesunięcie poziome", font=(16))
        label1.grid(column=1, row=2, columnspan=2, sticky=(tk.W, tk.N), pady=(12, 0))
        self.slider_offset = tk.Scale(root, from_=0, to=1700, orient=tk.HORIZONTAL)
        self.slider_offset.grid(column=1, row=3, columnspan=2, sticky=(tk.W, tk.E))
        self.slider_offset.set(0)
        label2 = tk.Label(root, text="przesunięcie pionowe", font=(16))
        label2.grid(column=1, row=4, columnspan=2, sticky=(tk.W), pady=(12, 0))
        self.slider_initial = tk.Scale(root, from_=0, to=512, orient=tk.HORIZONTAL)
        self.slider_initial.grid(column=1, row=5, columnspan=2, sticky=(tk.W, tk.E))
        button_update = tk.Button(root, text="aktualizuj", command=self.update_plot)
        button_update.grid(column=1, row=6)
        button_close = tk.Button(root, text="zamknij", command=exit)
        button_close.grid(column=2, row=6)

    def plot(self, *args):
        if self.drawing:
            self.drawing.destroy()
        img = []
        width = 734.4
        initial_offset = int((31.3363)*self.rate) + int(0*width) + self.initial_custom_offset
        for i in range(self.custom_offset, 512+self.custom_offset): #512
            line_offset = int(i*width)
            img.append(self.datal[
                initial_offset + line_offset
                : initial_offset + line_offset + int(width)
                ])
        img2 = [[] for _ in range(len(img[0]))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                img2[j].append(img[i][j])
        self.f = plt.figure(dpi=100)
        plt.axis("off")
        plt.imshow(img2, cmap=plt.get_cmap("Greys"), aspect=0.59)
        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.drawing = self.canvas.get_tk_widget()
        self.drawing.grid(column=1, row=1, columnspan=2, sticky=(tk.N))

    def update_plot(self):
        self.custom_offset = self.slider_offset.get()
        self.initial_custom_offset = self.slider_initial.get()
        self.plot()
        self.canvas.draw()

root = tk.Tk()
root.title("voyager decoder")
app = Application(root, "voy2.wav")
root.mainloop()
root.destroy()
