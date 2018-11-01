import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
# from sklearn.preprocessing import normalize
import scipy.io.wavfile

rate, data = scipy.io.wavfile.read('voy.wav')

# data = normalize(data)
datal = [s[0] for s in data]
datar = [s[1] for s in data]

img = []
width = 734.4
offset = int((31.3363)*rate) + int(0*width)
for i in range(512): #512
    offset2 = int(i*width)
    img.append(datal[offset + offset2 : offset + offset2 + int(width)])
f = plt.figure(dpi=200)
plt.imshow(img, cmap=plt.get_cmap("Greys"))
# plt.show()

root = tk.Tk()
root.title("just testing")
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack()
tk.mainloop()
