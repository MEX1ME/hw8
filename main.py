# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник
# с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр,
# сохранение, импорт, поиск, удаление.

import sqlite3 as sl


con = sl.connect("gb.db")  # соединяемся с бд. если ее нет, то создаем такую бд
cur = con.cursor()  # создаем указатель. через него будем выполнять запросы


def create_table():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT,
                phone INTEGER
                )"""
    )
    con.commit()


def search_by_name():
    print(
        """Введите данные для поиска
          1 - Имя
          2 - Фамилия
          3 - Номер"""
    )
    commands = {1: "name", 2: "surname", 3: "phone"}
    inp_command = int(input("Введи число: "))
    search_arg = input(f"Введите {commands.get(inp_command)} : ")
    cur.execute(
        f"select * from users where {commands.get(inp_command)} = '{search_arg}'"
    )
    for row in cur.fetchall():
        print(row)


def show_data():
    cur.execute("select * from users")
    for row in cur.fetchall():
        print(row)


def add_into_empty():  # если таблица пустая то добавить
    cur.execute("select * from users")
    if not cur.fetchall():
        cur.execute(
            "INSERT INTO users (name, surname, phone) VALUES ('Светофоров','Дорог','8321321321')"
        )
        con.commit()


def add_contact():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Номер: ")
    cur.execute(
        f"INSERT INTO users (name, surname, phone) VALUES ('{name}','{surname}','{phone}')"
    )
    con.commit()
    print("Контакт добавлен")


def delete_by_name():
    print(
        """Введите данные контакта для удаления
          1 - Имя
          2 - Фамилия
          3 - Номер"""
    )
    commands = {1: "name", 2: "surname", 3: "phone"}
    inp_command = int(input("Введи число: "))
    search_arg = input(f"Введите {commands.get(inp_command)} : ")
    cur.execute(f"DELETE FROM users WHERE {commands.get(inp_command)} = '{search_arg}'")
    con.commit()
    print("Контакт успешно удален.")


create_table()
add_into_empty()
show_data()

while True:
    print(
        """
          Добавить контакт - 1
          Посмотреть контакты - 2
          Поиск контакта - 3
          Удалить контакт - 4"""
    )
    inputNum = int(input("Выберите одно из действий "))
    if inputNum == 1:
        add_contact()
    if inputNum == 2:
        show_data()
    if inputNum == 3:
        search_by_name()
    if inputNum == 4:
        delete_by_name()
