import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory

import webbrowser
import os


from PIL import Image
import numpy as np
import functools
import threading


def work_mkdir():
    if os.path.exists('D:\Stick Figure Image'):
        pass
    else:
        os.mkdir('D:\Stick Figure Image')

work_mkdir()
os.chdir('D:\Stick Figure Image')
path = os.getcwd()
path_image = '{0}\Image'.format(path)


def one_image_re(numbers):
    screen2.delete(1.0, tk.END)
    start = image_path
    print
    U = 'Converting--Image: ' + start
    screen2.insert('insert', U+'\n')
    sta = image_path
    end = './' + 'Image/' + str(start[-5:])
    a = np.asarray(Image.open(sta).convert('L')).astype('float')
    depth = numbers
    grad = np.gradient(a)
    grad_x, grad_y = grad
    grad_x = grad_x * depth / 100.
    grad_y = grad_y * depth / 100.
    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A
    vec_el = np.pi / 2.2
    vec_az = np.pi / 4.
    dx = np.cos(vec_el) * np.cos(vec_az)
    dy = np.cos(vec_el) * np.sin(vec_az)
    dz = np.sin(vec_el)
    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
    b = b.clip(0, 255)
    im = Image.fromarray(b.astype('uint8'))
    im.save(end)
    screen2.insert('insert', 'The image has already converted into stick figure.')


def exists_mkdir():
    if os.path.exists('Image'):
        pass
    else:
        os.mkdir('Image')


def print_selection(v):
    global v1
    l.config(text='The value you chose: ' + v)
    v1 = v


def print_image_path(image_path):
    l2.config(text='The image path is: ' + image_path)


def main_one_images():
    print(v1)
    if int(v1) == 0:
        c["text"] = "The program is wrong because the parameter is not selected."
        pass

    else:
        try:
            next_work = tk.messagebox.askyesno(title='Prompt', message='Are you sure to do the next step,'
                                                                       'it may spend a couple '
                                                                       'seconds.')
            print(next_work)
            if next_work == True:
                numbers = int(v1)
                image_1 = functools.partial(one_image_re, numbers=numbers)
                p = threading.Thread(target=image_1)
                p.start()
                print((threading.activeCount() - 1))
                tk.messagebox.showinfo(title='Prompt', message='The software ran')
                if image_path is True:
                    c["text"] = c["text"] = "The program is running incorrectly, there may be no path selected " \
                                            "or the " \
                                            "configuration file is missing.\n(Don't solve? See the issues on the menu)"
                else:
                    c["text"] = "The software can successfully run.Please go to: " + path_image + '. to find the image'
            else:
                pass

        except (NameError, Exception):
            c["text"] = "The program is running incorrectly, there may be no path selected or the configuration " \
                        "file is" \
                        " missing.\n(Don't solve? See the issues on the menu)"


def window_1():
    tk.messagebox.showinfo(title='Manual', message=text_1)
def window_2():
    tk.messagebox.showinfo(title='Common Issues', message=text_2)
def window_3():
    tk.messagebox.showinfo(title='Author', message='Richard')


def open_image():
    global image_path
    image_path = filedialog.askopenfilename()
    print_image_path(image_path)
    print(image_path)


def open_images_path():
    webbrowser.open( os.getcwd() + '\Image')

window = tk.Tk()
window.geometry('600x300')
window.resizable(False, False)

menubar = tk.Menu(window)

firstmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Usage', menu=firstmenu)
firstmenu.add_command(label='How to use this converter',command=window_1)

thirdmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Issues', menu=thirdmenu)
thirdmenu.add_command(label='Common Issues', command=window_2)

# secondmenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='About us', menu=secondmenu)
# secondmenu.add_command(label='Author', command=window_3)

text_1='This software can help you convert any colorful image into stick figure form.\nStep1:  Select the image file.\nStep2:  ' \
       'Select a value from 0-100. The higher the value, the darker the color.(The standard parameter is 10)\nStep3:  ' \
       'Click "Convert" to confirm the single image(corresponding to the previous selection). ' \
       'Wait for a few seconds.\nFinally:  Click "Open Image Folder" to enter picture folder to find the stick figure picture'

text_2='Why i cannot find the stick figure image although the software said successfully run?\nBecause of this software was written' \
       'by numpy and pillow, so it had the limits on the size of image.We recommend you use some drawing tools to decrease the size of' \
       'the image and tried.'

window.config(menu=menubar)
window.title('image converter')
exists_mkdir()

b = Button(window,text='Select image',command=open_image)
b.place(x=10, y=10)

l2 = tk.Label(window, fg='#002d04', width=70, text='')
l2.place(x=130, y=13)

l = tk.Label(window, bg='lightskyblue', width=20, text='empty')
l.place(x=220, y=50)

s = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL,
             length=580, showvalue=0, tickinterval=10, resolution=1, command=print_selection)
s.place(x=5, y=85)

b = Button(window, text='Convert', command=main_one_images)
b.place(x=10, y=155)

c = tk.Label(window, text="")
c.place(x=0, y=190)

b = Button(window,text='Open Image Folder', command=open_images_path)
b.place(x=100, y=155)

screen2 = tk.Text(window, height=2, width=75)
screen2.place(x=30, y=235)

screen3 = tk.Label(window, text="First time? See the usage.")
screen3.place(x=440, y=280)

window.mainloop()