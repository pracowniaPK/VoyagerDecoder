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
        self.create_widgets()

    def create_widgets(self):
        self.plot()
        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.canvas.get_tk_widget().grid(column=1, row=1, columnspan=2, sticky=(tk.N))
        self.slider_offset = tk.Scale(root, from_=0, to=70, orient=tk.HORIZONTAL)
        self.slider_offset.grid(column=1, row=2, columnspan=2, sticky=(tk.W, tk.E))
        self.slider_offset.set(0)
        button_update = tk.Button(root, text="aktualizuj", command=self.update_plot)
        button_update.grid(column=1, row=4)
        button_close = tk.Button(root, text="zamknij", command=exit)
        button_close.grid(column=2, row=4)

    def plot(self):
        img = []
        width = 734.4
        initial_offset = int((31.3363)*self.rate) + int(0*width)
        self.custom_offset = 0
        for i in range(self.custom_offset, 512+self.custom_offset): #512
            line_offset = int(i*width)
            img.append(self.datal[
                initial_offset + line_offset
                : initial_offset + line_offset + int(width)
                ])
        self.f = plt.figure(dpi=100)
        plt.imshow(img, cmap=plt.get_cmap("Greys"))

    def update_plot(self):
        self.custom_offset = self.slider_offset.get()
        self.plot()
        self.canvas.draw()

# rate, data = scipy.io.wavfile.read('voy.wav')
# datal = [s[0] for s in data]
# datar = [s[1] for s in data]

# img = []
# width = 734.4
# offset = int((31.3363)*rate) + int(0*width)
# for i in range(512): #512
#     offset2 = int(i*width)
#     img.append(datal[offset + offset2 : offset + offset2 + int(width)])
# f = plt.figure(dpi=100)
# plt.imshow(img, cmap=plt.get_cmap("Greys"))


root = tk.Tk()
root.title("voyager decoder")
app = Application(root, "voy.wav")
root.mainloop()
root.destroy()
