import tkinter as tk
import time
import camera as cam

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
        c.render()

        window.update()
        label_text.set("FPS: " + str(int(1 / (time.time() - t))))
        t = time.time()

        pos = c.pos.v
        pos_label_text.set(
            "".join(["[", str(round(pos[0], 2)), ", ", str(round(pos[1], 2)), ", ", str(round(pos[2], 2)), "]"]))

        rot = c.rot.q
        rot_label_text.set(
            "".join(["[", str(round(rot[0], 3)), ", ", str(round(rot[1], 3)), ", ", str(round(rot[2], 3)), ", ", str(round(rot[3], 3)), "]"]))

        window.after(MS_PER_TICK, tick)

    def key_event(event):
        if event.char == 'w':
            c.move_forward(10 / FPS)
        elif event.char == 'a':
            c.move_left(10 / FPS)
        elif event.char == 's':
            c.move_backward(10 / FPS)
        elif event.char == 'd':
            c.move_right(10 / FPS)
        elif event.char == 'q':
            c.move_down(10 / FPS)
        elif event.char == 'e':
            c.move_up(10 / FPS)
        elif event.char == 'i':
            c.rotate_up(0.1 / FPS)
        elif event.char == 'j':
            c.rotate_left(0.1 / FPS)
        elif event.char == 'k':
            c.rotate_down(0.1 / FPS)
        elif event.char == 'l':
            c.rotate_right(0.1 / FPS)
        elif event.char == 'u':
            c.rotate_ccw(0.1 / FPS)
        elif event.char == 'o':
            c.rotate_cw(0.1 / FPS)
        pass

    window = tk.Tk()
    window.title("camera-test")
    window.resizable(False, False)

    canvas = tk.Canvas(
        window, bg="black", width=W, height=H, bd=-2)
    canvas.pack()

    label_text = tk.StringVar()
    label_text.set("FPS: ")
    label = tk.Label(window, textvariable=label_text, width=7,
                     height=1, fg="white", bg="black", bd=0, anchor="nw")
    label.place(in_=canvas, relx=0, rely=0)

    pos_label_text = tk.StringVar()
    pos_label_text.set("[]")
    pos_label = tk.Label(window, textvariable=pos_label_text,
                         width=40, height=1, fg="white", bg="black", bd=0, anchor="nw")
    pos_label.place(in_=canvas, relx=0, rely=0.05)

    rot_label_text = tk.StringVar()
    rot_label_text.set("[]")
    rot_label = tk.Label(window, textvariable=rot_label_text,
                         width=40, height=1, fg="white", bg="black", bd=0, anchor="nw")
    rot_label.place(in_=canvas, relx=0, rely=0.1)

    # create camera
    c = cam.Camera(2 * math.pi / 3, canvas)

    # keyboard event
    window.bind("<Key>", key_event)

    window.after(MS_PER_TICK, tick)

    window.mainloop()
