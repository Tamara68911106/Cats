from tkinter import*
from PIL import Image,ImageTk
import requests
from io import BytesIO # позволяет работать с двоичными (1,0) байтами,т.к картинка из инета будет приходить в виде набора байтов, ее(картинку) надо превратить в изображение

window = Tk()# создаем окно
window.title("Cats!")# заголовок
window.geometry("600x480")

label = Label() # метка
label.pack()

url = "https: // cataas.com/cat" # адрес интернете
img = load_image(url)


if img: # если картинка не путая
    label.config(image=img)
    label.image = img # картинка происвоина и сборщик мусора ее не удалит



window.mainloop()
