from tkinter import *

from model import Session
from view.car_view import CarView
from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.maintenance_view import MaintenanceView
from view.sale_view import SaleView

class DashboardView:
    def car_view(self):
        ui = CarView()


    def customer_view(self):
        ui = CustomerView()


    def employee_view(self):
        ui = EmployeeView()

    def maintenance_view(self):
        ui = MaintenanceView()

    def sale_view(self):
        ui = SaleView()


    def __init__(self):
        self.employee = Session.employee
        font = ("Arial", 18, "bold")
        width = 24
        background_color = "violet red"
        foreground_color = "white"

        y_dist = 60

        self.window = Tk()
        self.window.geometry("540x900")
        self.window.title("Dashboard")
        self.window.config(bg="white")

        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Car",
           command=self.car_view).place(x=80, y=180)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Customer",
           command=self.customer_view).place(x=80, y=180 + y_dist * 1)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Employee",
           command=self.employee_view).place(x=80, y=180 + y_dist * 2)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Maintenance",
           command=self.maintenance_view).place(x=80, y=180 + y_dist * 3)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Sale",
           command=self.sale_view).place(x=80, y=180 + y_dist * 4)

        self.window.mainloop()
