from tkinter import*
from PIL import Image,ImageTk
import requests
from io import BytesIO # позволяет работать с двоичными (1,0) байтами,т.к картинка из инета будет приходить в виде набора байтов, ее(картинку) надо превратить в изображение

from bottle import response
from gevent.testing.travis import command


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)# функция возвращает img
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def set_image():
    img = load_image(url)

    if img:  # если картинка не пустая
        label.config(image=img)
        label.image = img  # картинка происвоина и сборщик мусора ее не удалит


def exit():
    window.destroy() #окошко будет уничтожено, программа завершена

window = Tk()# создаем окно
window.title("Cats!")# заголовок
window.geometry("600x520")

label = Label() # метка
label.pack()


url = "https://cataas.com/cat" # адрес интернете
img = load_image(url)


#update_button = Button(text="Обновить", command=set_image)
#update_button.pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)# чтобы меню не отклеивалось
menu_bar.add_cascade(label= "Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add.command(lebel = "Выход", command=exit)


set_image()

window.mainloop()
