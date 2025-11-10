from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image as PILImage

from controller import EmployeeController
from model import Session

from view.dashboard_view import DashboardView


class LoginView:
    def __init__(self):
        self.employee_controller = EmployeeController()
        self.window = Tk()
        self.window.title("Employee Login")
        self.window.config(background="white")
        self.window.geometry("300x550")

        image = PILImage.open("images/user.png")
        image = image.resize((160, 160), PILImage.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        Label(self.window, image=self.image, bg="white").place(x=70, y=25)

        self.username_label = Label(self.window, text="Username:", bg="white", font=("Arial", 12))
        self.username_label.place(x=30, y=250)
        self.username_entry = Entry(self.window, width=25, font=("Arial", 12))
        self.username_entry.place(x=30, y=275)

        self.password_label = Label(self.window, text="Password:", bg="white", font=("Arial", 12))
        self.password_label.place(x=30, y=310)
        self.password_entry = Entry(self.window, width=25, show="*", font=("Arial", 12))
        self.password_entry.place(x=30, y=335)

        self.username_entry.insert(0, "reza4321")
        self.password_entry.insert(0, "ali12345678")

        Button(
            self.window,
            text="Login",
            width=8,
            font=("Arial", 14),
            bg="midnight blue",
            fg="white",
            command=self.login
        ).place(x=50, y=380, width=200, height=60)

        Button(
            self.window,
            text="Continue as Guest",
            width=16,
            font=("Arial", 12),
            bg="lightgray",
            command=self.guest_mode
        ).place(x=65, y=460, width=170, height=45)

        self.window.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        status, employee = self.employee_controller.find_by_username_and_password(username, password)

        if status:
            Session.employee = employee
            self.window.destroy()
            DashboardView()
        else:
            messagebox.showerror("Login Error", "Access Denied !!!")

    def guest_mode(self):
        Session.employee = None
        self.window.destroy()
        DashboardView()
