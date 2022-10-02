from bisect import bisect_right
import imghdr
from importlib.resources import path
from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.image as mpimg
from jupiter_image import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

global r_path
r_path = None
global g_path
g_path = None
global b_path
b_path = None
global raw_path
raw_path = None
global map_path
map_path = None
global bright_value
bright = None
global img
img = None
global figure
figure = None
global img_new
img_new = None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1600x994")
window.configure(bg = "#FFFFFF")

current_value_bright = tk.DoubleVar()
current_value_color = tk.DoubleVar()
current_value_contrast = tk.DoubleVar()

def get_current_value_bright():
    global bright_value
    bright_value = '{: .2f}'.format(current_value_bright.get())

def slider_bright_changed(event):
    value_bright_label.configure(text=get_current_value_bright())

def get_current_value_color():
    color_value = '{: .2f}'.format(current_value_color.get())
    return color_value

def slider_color_changed(event):
    value_color_label.configure(text=get_current_value_color())

def get_current_value_contrast():
    contrast_value = '{: .2f}'.format(current_value_contrast.get())
    return contrast_value

def slider_contrast_changed(event):
    value_contrast_label.configure(text=get_current_value_contrast())

def open_file(text):
    global raw_path
    global r_path
    global g_path
    global b_path
    global map_path

    path = filedialog.askdirectory(initialdir ='C:\\Users\\agust.AGUSTIN_PC\\Documents\\MEGAsync\\Facultad\\Tercer año\\', 
                                            title='Select folder')

    text['text'] = path 

    images = os.listdir(path)

    for image in images:
        if re.findall('raw', image):
            raw_path = path + '/' + image
        if re.findall('red', image):
            r_path = path + '/' + image
        if re.findall('green', image):
            g_path = path + '/' + image
        if re.findall('blue', image):
            b_path = path + '/' + image
        if re.findall('mapprojected', image):
            map_path = path + '/' + image

    show_raw(raw_path)

def show_raw(raw_path):
    global img
    global figure
    figure = plt.figure(figsize=(5, 5), dpi=140)
    img = mpimg.imread(str(raw_path))
    plt.imshow(img)

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=600,y=253)

def show_red(red_path):
    global img
    global figure
    figure = plt.figure(figsize=(5, 5), dpi=140)
    img = processSingleChannel(red_path)
    plt.imshow(img)

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=600,y=253)

def show_green(green_path):
    global img
    global figure
    figure = plt.figure(figsize=(5, 5), dpi=140)
    img = processSingleChannel(green_path)
    plt.imshow(img)

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=600,y=253)  

def show_blue(map_path):
    global img
    global figure
    figure = plt.figure(figsize=(5, 5), dpi=140)
    img = processMapImage(map_path)
    plt.imshow(img)

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=600,y=253)

def show_rgb(r_path, g_path, b_path):
    global img
    global figure
    global img_new
    figure = plt.figure(figsize=(5, 5), dpi=140)
    img = processImageByChannels(r_path, g_path, b_path)
    plt.imshow(img)
    process()

def process():
    global figure
    global img_new
    global bright_value
    bright_value = int(round(float(bright_value)))
    #img_new = increase_brightness(img, bright_value)
    img_new = change_brightness(img, bright_value)
    plt.imshow(img_new)

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=600,y=253)


def show_info():
    messagebox.showinfo('FAQ', 'Project made by Jupiter Nexus Team\n\n Members:\n  > Mariano Sanchez Toledo\n  > Agustín Montaña\n  > Florencia Cisterna\n  > Emilia Videla\n  > Oriel Barroso\n  > Mar Quijano\n\n 2022')

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

canvas_plot = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas_plot.place(x = 600, y = 253)

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
    x=63.0,
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
    x=28.0,
    y=886.0,
    width=326.0,
    height=70.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_info(),
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
    command=lambda: show_raw(raw_path),
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
    command=lambda: show_red(r_path),
    relief="flat"
)
button_5.place(
    x=1516.0,
    y=344.0,
    width=105.0,
    height=79.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_green(g_path),
    relief="flat"
)
button_6.place(
    x=1516.0,
    y=426.0,
    width=105.0,
    height=79.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_blue(map_path),
    relief="flat"
)
button_7.place(
    x=1516.0,
    y=510.0,
    width=105.0,
    height=79.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_rgb(r_path, g_path, b_path),
    relief="flat"
)
button_8.place(
    x=1516.0,
    y=594.0,
    width=105.0,
    height=79.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: process(),
    relief="flat"
)
button_10.place(
    x=26.0,
    y=699.0,
    width=326.0,
    height=70.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    947.5,
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
    x=467.0,
    y=158.0,
    width=961.0,
    height=48.0
)

slider_bright = Scale(
    window,
    from_=-127,
    to=127,
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