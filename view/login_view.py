from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image as PILImage

from controller import EmployeeController
from model import Session
from view import DashboardView
from view import LabelWithEntry


class LoginView:
    def __init__(self):
        self.employee_controller = EmployeeController()
        self.window = Tk()
        self.window.title("Employee Login")
        self.window.config(background="white")
        self.window.geometry("300x550")

        image = PILImage.open("./view/images/user.png")
        image = image.resize((160, 160), PILImage.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        Label(self.window, image=self.image, bg="white").place(x=70, y=25)

        self.username = LabelWithEntry(
            self.window, "Username", 30, 250, distance=100, data_type=StringVar
        )
        self.password = LabelWithEntry(
            self.window, "Password", 30, 310, distance=100, data_type=StringVar
        )

        self.username.set("reza4321")
        self.password.set("ali12345678")

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
        username = self.username.get()
        password = self.password.get()

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
