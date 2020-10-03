import tkinter as tk
import time

# resolution
W = 480
H = 360

# fps
FPS = 30
MS_PER_TICK = int(1000 / FPS) - 1

if __name__ == "__main__":

    t = time.time()

    def tick():
        global t

        # Update Canvas

        window.update()
        label_text.set("FPS: " + str(int(1 / (time.time() - t))))
        t = time.time()

        window.after(MS_PER_TICK, tick)

    window = tk.Tk()
    window.title("camera-test")
    window.resizable(False, False)

    canvas = tk.Canvas(
        window, bg="black", width=W, height=H, bd=-2)
    canvas.pack()

    label_text = tk.StringVar()
    label_text.set("FPS: ")
    label = tk.Label(window, textvariable=label_text, width=7,
                     height=1, fg="white", bg="black", bd=0)
    label.place(in_=canvas, relx=0, rely=0)

    window.after(MS_PER_TICK, tick)

    window.mainloop()
