from tkinter import*
from PIL import Image,ImageTk
import requests
from io import BytesIO # позволяет работать с двоичными (1,0) байтами,т.к картинка из инета будет приходить в виде набора байтов, ее(картинку) надо превратить в изображение

from bottle import response


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_date=BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)# функция возвращает img
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def set_image():
    img = load_image(url)

    if img:  # если картинка не пустая
        label.config(image=img)
        label.image = img  # картинка происвоина и сборщик мусора ее не удалит


window = Tk()# создаем окно
window.title("Cats!")# заголовок
window.geometry("600x480")

label = Label() # метка
label.pack()

update_button = Button("Обновить", command=set_image)
update_button.pack()

url = "https: // cataas.com/cat" # адрес интернете

set_image()

window.mainloop()
