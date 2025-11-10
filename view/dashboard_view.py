from tkinter import *
from PIL import ImageTk, Image
from model import Session
from view.car_view import CarView
from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.maintenance_view import MaintenanceView
from view.sale_view import SaleView


class DashboardView:
    def __init__(self):
        self.employee = Session.employee
        font = ("Arial", 18, "bold")
        width = 24
        background_color = "midnight blue"
        foreground_color = "white"

        y_dist = 60

        self.window = Tk()
        self.window.geometry("540x560")
        self.window.title("Dashboard")
        self.window.config(bg="white")

        image = Image.open("./view/images/logo.png")
        image = image.resize((400, 160), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        Label(self.window, image=self.image, bg="white").place(x=70, y=15)

        self.buttons = {}
        names = ["Car", "Customer", "Employee", "Maintenance", "Sale"]
        commands = [self.car_view, self.customer_view,
                    self.employee_view, self.maintenance_view, self.sale_view]

        for i, (name, cmd) in enumerate(zip(names, commands)):
            btn = Button(self.window, font=font, width=width,
                         bg=background_color, fg=foreground_color,
                         text=name, command=cmd)
            btn.place(x=80, y=180 + y_dist * i)
            self.buttons[name] = btn

        employee_name = self.employee.username if self.employee else "Not Logged In"
        Label(self.window, text=f"Employee : {employee_name}",
              font=font, bg="white").place(x=80, y=500)

        if not self.employee:
            for name in ["Employee", "Maintenance", "Sale"]:
                btn = self.buttons[name]
                btn.config(state=DISABLED, bg="gray80")

        self.window.mainloop()

    def car_view(self):
        CarView()

    def customer_view(self):
        CustomerView()

    def employee_view(self):
        EmployeeView()

    def maintenance_view(self):
        MaintenanceView()

    def sale_view(self):
        SaleView()
