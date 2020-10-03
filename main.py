import tkinter as tk

# resolution
W = 480
H = 360

if __name__ == "__main__":
    window = tk.Tk()
    window.title("camera-test")
    window.resizable(False, False)

    canvas = tk.Canvas(window, bg="black", width=W, height=H)

    canvas.pack()

    window.mainloop()
