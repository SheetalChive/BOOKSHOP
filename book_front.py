from tkinter import *
import book_back


win = Tk()
win.geometry("450x480")
win.title("BookShop")


def view_btn():
    List_box.delete(0,END)
    for row in book_back.view():
        List_box.insert(END,row)

def add_btn():
    book_back.insert(book_value.get(),author_value.get(),year_value.get(),id_value.get())
    view_btn()


def get_selected_row(event):
    global get_tuple
    index = List_box.curselection()[0]
    get_tuple = List_box.get(index)
    print(get_tuple)
    clear()
    book_Entry.insert(END,get_tuple[1])
    author_Entry.insert(END,get_tuple[2])
    year_Entry.insert(END,get_tuple[3])
    book_id_Entry.insert(END,get_tuple[4])


def del_btn():
    book_back.delete(get_tuple[0])
    view_btn()
    clear()


def update_btn():
    book_back.update(book_value.get(),author_value.get(),year_value.get(),id_value.get(), get_tuple[0])
    
    view_btn()
# def del_btn():
    
    
#     clear()
#     index = List_box.curselection()[0




#     get_tuple = List_box.delete(index)
#     book_Entry.delete(END,)
#     author_Entry.delete(END,)
#     year_Entry.delete(END,)
#     book_id_Entry.delete(END,)


def clear():
    book_Entry.delete(0,END)
    author_Entry.delete(0,END)
    year_Entry.delete(0,END)
    book_id_Entry.delete(0,END)

title_lable = Label(win,text = "BOOKSHOP",font = ('arial',18,'bold'))
title_lable.place(x=130,y =20, width = 200,height =20)

book_lable = Label(win,text = "BOOK")
book_lable.place(x = 10, y = 70 ,width = 100, height = 30)

book_value = StringVar()
book_Entry = Entry(win,textvariable = book_value)
book_Entry.place(x = 110, y = 70 ,width = 100, height = 30)


author_lable = Label(win,text = "AUTHOR")
author_lable.place(x = 210, y = 70 ,width = 100, height = 30)

author_value = StringVar()
author_Entry = Entry(win,textvariable = author_value)
author_Entry.place(x = 320, y =70 ,width = 100, height = 30)


year_lable = Label(win,text = "YEAR")
year_lable.place(x = 10, y = 110 ,width = 100, height = 30)
year_value = StringVar()
year_Entry = Entry(win,textvariable = year_value)
year_Entry.place(x = 110, y = 110 ,width = 100, height = 30)


book_id_lable = Label(win,text = "ISBN")
book_id_lable.place(x = 210, y = 110 ,width = 100, height = 30)

id_value = StringVar()
book_id_Entry = Entry(win,textvariable = id_value)
book_id_Entry.place(x = 320, y =110 ,width = 100, height = 30)

button_add = Button(win,text = "ADD",command = add_btn)
button_add.place(x = 30 , y = 350,width = 100 , height = 30)

button_delete = Button(win,text = "DELETE",command = del_btn)
button_delete.place(x = 180 , y = 350,width = 100 , height = 30)

button_view = Button(win,text = "VIEW",command = view_btn)
button_view.place(x = 30 , y = 400,width = 100 , height = 30)

button_update = Button(win,text = "UPDATE",command = update_btn)
button_update.place(x = 180 , y = 400,width = 100 , height = 30)

button_search = Button(win,text = "SEARCH")
button_search.place(x = 320 , y = 350,width = 100 , height = 30)

button_clear = Button(win,text = "CLEAR",command = clear)
button_clear.place(x = 320 , y = 400,width = 100 , height = 30)


List_box = Listbox(win)
List_box.place(x = 30 , y =160,width = 390 , height = 170)
List_box.bind('<<ListboxSelect>>',get_selected_row)




# display()

win.mainloop()