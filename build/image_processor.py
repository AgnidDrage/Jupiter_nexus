from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, filedialog, messagebox
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1600x994")
window.configure(bg = "#FFFFFF")

current_value_bright = tk.DoubleVar()
current_value_color = tk.DoubleVar()
current_value_contrast = tk.DoubleVar()

def get_current_value_bright():
    return '{: .2f}'.format(current_value_bright.get())

def slider_bright_changed(event):
    value_bright_label.configure(text=get_current_value_bright())

def get_current_value_color():
    return '{: .2f}'.format(current_value_color.get())

def slider_color_changed(event):
    value_color_label.configure(text=get_current_value_color())

def get_current_value_contrast():
    return '{: .2f}'.format(current_value_contrast.get())

def slider_contrast_changed(event):
    value_contrast_label.configure(text=get_current_value_contrast())

def open_file(text):
    
    archivo = filedialog.askopenfilename(initialdir ='C:\\Users\\agust.AGUSTIN_PC\\Documents\\MEGAsync\\Facultad\\Tercer año\\', 
                                        title='Selecione archivo', 
                                        filetypes=(('png files', '*.png*'),('All files', '*.*')))
    
    # read_data(archivo) Aca va la funcion para cargar el archivo
    text['text'] = archivo 

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 994,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    800.0,
    512.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file(entry_1),
    relief="flat"
)
button_1.place(
    x=26.0,
    y=158.0,
    width=252.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1331.0,
    y=158.0,
    width=252.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1526.0,
    y=45.0,
    width=57.0,
    height=51.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1516.0,
    y=257.0,
    width=105.0,
    height=79.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=1516.0,
    y=344.0,
    width=105.0,
    height=79.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    802.5,
    183.0,
    image=entry_image_1
)
entry_1 = Label(
    bd = 0,
        bg = "#FFFFFF",
        highlightthickness = 0,
        font=('Nunito 12'),
        justify=LEFT
)
entry_1.place(
    x=322.0,
    y=158.0,
    width=961.0,
    height=48.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    947.0,
    610.0,
    image=image_image_2
)

slider_bright = Scale(
    window,
    from_=-50,
    to=50,
    orient='horizontal',
    command=slider_bright_changed,
    variable=current_value_bright,
    background='#868789',
    highlightcolor='#868789',
    highlightbackground='#868789',)

slider_bright.place(
    x=30,
    y=360,
    width=320,
    height=48.0
)

slider_color = Scale(
    window,
    from_=-50,
    to=50,
    orient='horizontal',
    command=slider_color_changed,
    variable=current_value_color,
    background='#868789',
    highlightcolor='#868789',
    highlightbackground='#868789',)

slider_color.place(
    x=30,
    y=470,
    width=320,
    height=48.0
)

slider_contrast = Scale(
    window,
    from_=-50,
    to=50,
    orient='horizontal',
    command=slider_contrast_changed,
    variable=current_value_contrast,
    background='#868789',
    highlightcolor='#868789',
    highlightbackground='#868789',)

slider_contrast.place(
    x=30,
    y=583,
    width=320,
    height=48.0
)

current_value_bright_label = Label(
    window,
    text='Current Value:'
)

value_bright_label = Label(
    window,
    text=get_current_value_bright()
)

current_value_color_label = Label(
    window,
    text='Current Value:'
)

value_color_label = Label(
    window,
    text=get_current_value_color()
)

current_value_contrast_label = Label(
    window,
    text='Current Value:'
)

value_contrast_label = Label(
    window,
    text=get_current_value_contrast()
)

window.resizable(False, False)
window.mainloop()
