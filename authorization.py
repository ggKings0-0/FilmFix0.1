# Importing dependencies
from tkinter import *
from tkinter import messagebox
import pickle

# Creating window
root = Tk()
root.geometry("300x500")
root.title('Войти в систему')

# Registration function
def register():
    text = Label(root, text="Для входа в систему - зарегиструйтесь!")
    text_log = Label(root, text='Введите Ваш логин: ')
    register_login = Entry(root)
    text_password1 = Label(root, text='Введите Ваш пароль: ')
    register_password1 = Entry(root, show='*')
    text_password2 = Label(root, text='Повторите пароль: ')
    register_password2 = Entry(root, show='*')
    button_register = Button(root, text='Зарегистрироваться!', command=lambda: save())
    text.pack()
    text_log.pack()
    register_login.pack()
    text_password1.pack()
    register_password1.pack()
    text_password2.pack()
    register_password2.pack()
    button_register.pack()

    def save():
        login_pass_save = {}
        login_pass_save[register_login.get()] = register_password1.get()
        f = open('login.txt', 'wb')
        pickle.dump(login_pass_save, f)
        f.close()
        register()

# Login function
def login():
    text_log = Label(root, text='Поздравляем! Теперь Вы можете войти в систему!')
    text_enter_login = Label(root, text='Введите Ваш логин: ')
    enter_login = Entry(root)
    text_enter_password = Label(root, text='Введите Ваш пароль: ')
    enter_password = Entry(root, show='*')
    button_login = Button(root, text='Войти в систему!', command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_login.pack()

    def log_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo('Success', 'Войдите в систему!')
            else:
                messagebox.showerror('Error', 'Неверный пароль!')
        else:
            messagebox.showerror('Error', 'Неверный логин!')
        login()
root.mainloop()
