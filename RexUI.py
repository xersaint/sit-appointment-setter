import tkinter as tk
from tkinter import ttk

# import mariadb
import mysql.connector
# import sys

root = tk.Tk()
root.configure(bg='#F5F5DC')
root.title("Appointment Setter")
root.geometry("600x400")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="appointment_system"
)

# # Connect to MariaDB Platform
# try:
#     conn = mariadb.connect(
#         user="root",
#         password="",
#         host="127.0.0.1",
#         port=3306,
#         database="appointment_system"
#
#     )
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)
#
# # Get Cursor
# cur = conn.cursor()

# cur.execute("USE appointment_system")
#
# cur.execute("CREATE TABLE IF NOT EXISTS appointment (id int PRIMARY KEY AUTO_INCREMENT PRIM, name VARCHAR(100), "
#             "date VARCHAR("
#             "10), time VARCHAR(10))")

mysqlCur = mydb.cursor()
mysqlCur.execute("CREATE TABLE IF NOT EXISTS appointment (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), "
                 "date VARCHAR("
                 "10), time VARCHAR(10))")

name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=(30, 0), pady=10, sticky="W")

name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=(0, 30), pady=10, columnspan=2, sticky="W")


def log_name_input():
    name = name_entry.get()
    name_label_output = ttk.Label(root, text=name)
    name_label_output.grid(row=0, column=3, padx=(0, 30), pady=10, columnspan=2, sticky="W")
    print(f"Name input: {name}")


# name_entry.bind("<FocusOut>", log_name_input)

date_label = ttk.Label(root, text="Date:")
date_label.grid(row=1, column=0, padx=(30, 0), pady=10, sticky="W")

date_entry = ttk.Entry(root)
date_entry.grid(row=1, column=1, padx=(0, 30), pady=10, columnspan=2, sticky="W")


def log_date_input():
    date = date_entry.get()
    date_label_output = ttk.Label(root, text=date)
    date_label_output.grid(row=1, column=3, padx=(0, 30), pady=10, columnspan=2, sticky="W")
    print(f"Date input: {date}")


# date_entry.bind("<FocusOut>", log_date_input)

time_label = ttk.Label(root, text="Time:")
time_label.grid(row=2, column=0, padx=(30, 0), pady=10, sticky="W")

time_entry = ttk.Entry(root)
time_entry.grid(row=2, column=1, padx=(0, 30), pady=10, columnspan=2, sticky="W")


def log_time_input():
    time = time_entry.get()
    time_label_output = ttk.Label(root, text=time)
    time_label_output.grid(row=2, column=3, padx=(0, 30), pady=10, columnspan=2, sticky="W")
    print(f"Time input: {time}")


# time_entry.bind("<FocusOut>", log_time_input)


def set_appointment():
    name = name_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    log_name_input()
    log_date_input()
    log_time_input()

    sql = f"INSERT INTO appointment (name, date, time) VALUES(%s, %s, %s)"
    val = (name, date, time)
    mysqlCur.execute(sql, val)
    mydb.commit()

    name_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    time_entry.delete(0, 'end')

    response = f"Entry Added"

    entry_output = ttk.Label(root, text=response)
    entry_output.grid(row=5, column=3, padx=(0, 30), pady=10, columnspan=2, sticky="W")

    appointment_data = fetch_entries_by_table_name("appointment")

    for idx, i in enumerate(appointment_data):
        # entry_output = ttk.Label(root, text=i.name)
        # entry_output.grid(row=5, column=3, padx=(0, 30), pady=10, columnspan=2, sticky="W")
        print(i, idx)


def fetch_entries_by_table_name(table_name):
    my_db_cursor = mydb.cursor()
    mysql_query = f"SELECT * FROM {table_name}"
    my_db_cursor.execute(mysql_query)
    query_result = my_db_cursor.fetchall()
    my_db_cursor.close()

    return query_result


set_appointment_button = ttk.Button(root, text="Set Appointment", command=set_appointment)
set_appointment_button.grid(row=5, column=0, columnspan=2, pady=(10, 20))

root.mainloop()
