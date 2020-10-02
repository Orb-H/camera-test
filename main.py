import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    window.title("camera-test")
    window.resizable(False, False)

    canvas = tk.Canvas(window, bg="black", width=480, height=360) # change number for other resolution

    canvas.pack()

    window.mainloop()
