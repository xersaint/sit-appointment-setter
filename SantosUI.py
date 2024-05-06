import tkinter as tk
from tkinter import ttk


def exit_program():

    app.destroy()


def display_output():
        print("here")


class AppointmentSetting(tk.Tk):
    name = "Name:"
    name_label = ""
    date = "Date:"
    date_label = ttk.Label
    time = "Time:"
    time_label = ttk.Label
    submit_button = ttk.Button
    name_entry = ttk.Entry
    date_entry = ttk.Entry
    time_entry = ttk.Entry

    def __init__(self):
        super().__init__()

        self.title("Appointment Setting")
        self.geometry("1200x500")

        self.config(bg="#F5F5DC")

        self.create_labels_and_entries()
        self.create_submit_button()

    def create_labels_and_entries(self):

        self.name_label = ttk.Label(self, text=self.name, font=("Arial", 13, "bold"), foreground="#333")
        self.name_label.pack(pady=10)

        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=10)

        self.date_label = ttk.Label(self, text=self.date)
        self.date_label.pack(pady=10)

        self.date_entry = ttk.Entry(self)
        self.date_entry.pack(pady=10)

        self.time_label = ttk.Label(self, text="Time:")
        self.time_label.pack(pady=10)

        self.time_entry = ttk.Entry(self)
        self.time_entry.pack(pady=10)

    def create_submit_button(self):

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_appointment)
        self.submit_button.pack(pady=10)

    def submit_appointment(self):

        try:
            name = self.name_entry.get()
            date = self.date_entry.get()
            time = self.time_entry.get()

            print(f"Appointment details: Name - {name}, Date - {date}, Time - {time}")
            display_output()

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        self.destroy()


if __name__ == "__main__":
    app = AppointmentSetting()
    app.mainloop()
