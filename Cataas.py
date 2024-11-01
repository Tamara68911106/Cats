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

def open_new_window():
    tag = tag_entry.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat" # самый простой способ склейки - использовать fстроку
    img = load_image(url_tag)

    if img:  # если картинка не пустая
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img) # метка
        label.pack()
        label.image = img  # картинка происвоина и сборщик мусора ее не удалит


def exit():
    window.destroy() #окошко будет уничтожено, программа завершена

window = Tk()# создаем окно
window.title("Cats!")# заголовок
window.geometry("600x520")

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text="Загрузить по тегу", command = open_new_window)
load_button.pack()

url = "https://cataas.com/cat" # адрес интернете
img = load_image(url)


#update_button = Button(text="Обновить", command=set_image)
#update_button.pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)# чтобы меню не отклеивалось
menu_bar.add_cascade(label= "Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label = "Выход", command=exit)


window.mainloop()
