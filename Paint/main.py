import tkinter as tk
from tkinter import colorchooser

# окно программы
root = tk.Tk()
root.title("MyPaint")
root.geometry("800x600")

# состояние по умолчанию
current_color = "black"
brush_size = 5
is_erasing = False


# холст и его цвет
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)



def set_color():
    global current_color, mode
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
        mode = "brush"  # переключаемся на кисть после выбора цвета


def activate_eraser():
    global current_color, is_erasing
    is_erasing = True
    current_color = "white"  # цвет фона



def draw(event):
    x, y = event.x, event.y
    obj_id = canvas.create_oval( x - brush_size, y - brush_size, x + brush_size, y + brush_size, outline=current_color, fill=current_color)


panel = tk.Frame(root)
panel.pack()

tk.Button(panel, text="Выбрать цвет", command=set_color).pack(side=tk.LEFT)
tk.Button(panel, text="Ластик", command=activate_eraser).pack(side=tk.LEFT)

# рисование мышью
canvas.bind("<B1-Motion>", draw)


root.mainloop()
