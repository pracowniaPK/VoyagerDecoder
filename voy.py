import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
# from sklearn.preprocessing import normalize
import scipy.io.wavfile


class App:

    def __init__(self, master):
        master.title("just testing")
        frame = tk.Frame(master)
        frame.pack()

        img = give_img(width=734.4)
        fig = plt.figure(dpi=200)
        plt.imshow(img, cmap=plt.get_cmap("Greys"))
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()

        self.button = tk.Button(
            frame, text="QUIT", fg="red", command=frame.quit
        )
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("hi there, everyone!")


def give_img(width, length=512, left=True,):
    rate, data = scipy.io.wavfile.read('voy.wav')

    # data = normalize(data)
    track = [s[0] for s in data] if left else [s[1] for s in data]

    img = []
    offset = int((31.3363)*rate) + int(0*width)
    for i in range(length):
        offset2 = int(i*width)
        img.append(track[offset + offset2: offset + offset2 + int(width)])
    return img


root = tk.Tk()
app = App(root)

# canvas = FigureCanvasTkAgg(f, master=root)
# canvas.get_tk_widget().pack()

print(1)
root.mainloop()
print(2)
root.destroy()
print(3)
