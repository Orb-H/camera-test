import tkinter as tk
import time
import sys
import camera as cam
import math

# resolution
W = 480
H = 360

# fps
FPS = 30
MS_PER_TICK = int(1000 / FPS) - 1

if __name__ == "__main__":

    t = time.time()

    def tick():
        global t, fps_recent

        dis_x = window.winfo_pointerx() - window.winfo_rootx() - W / 2
        dis_y = window.winfo_pointery() - window.winfo_rooty() - H / 2
        c.rotate_down(c.fov / 2 * dis_y / c.r.s)
        c.rotate_right(c.fov / 2 * dis_x / c.r.s)

        window.event_generate("<Motion>", warp=True, x=W / 2, y=H / 2)

        # Update Canvas
        c.render()

        window.update()
        fps_now = int(1 / (time.time() - t))
        fps_recent = (9 * fps_recent + fps_now) / 10
        fps_label_text.set("FPS: " + str(fps_now) +
                           " / Recent FPS: " + str(int(fps_recent)))
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

    def close(event):
        sys.exit()

    window = tk.Tk()
    window.title("camera-test")
    window.resizable(False, False)
    window.config(cursor="none")

    canvas = tk.Canvas(
        window, bg="black", width=W, height=H, bd=-2)
    canvas.pack()

    fps_label_text = tk.StringVar()
    fps_label_text.set("FPS: / Recent FPS:")
    fps_label = tk.Label(window, textvariable=fps_label_text,
                         height=1, fg="white", bg="black", bd=0, anchor="nw")
    fps_label.place(in_=canvas, relx=0, rely=0)
    fps_recent = FPS

    pos_label_text = tk.StringVar()
    pos_label_text.set("[]")
    pos_label = tk.Label(window, textvariable=pos_label_text,
                         height=1, fg="white", bg="black", bd=0, anchor="nw")
    pos_label.place(in_=canvas, relx=0, rely=0.05)

    rot_label_text = tk.StringVar()
    rot_label_text.set("[]")
    rot_label = tk.Label(window, textvariable=rot_label_text,
                         height=1, fg="white", bg="black", bd=0, anchor="nw")
    rot_label.place(in_=canvas, relx=0, rely=0.1)

    window.event_generate("<Motion>", warp=True, x=W / 2, y=H / 2)

    # create camera
    c = cam.Camera(2 * math.pi / 3, canvas)

    # keyboard event
    window.bind("<Key>", key_event)
    window.bind("<Escape>", close)

    window.after(MS_PER_TICK, tick)

    window.mainloop()
