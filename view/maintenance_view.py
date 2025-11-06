from view import *
from model import Maintenance, Session
from controller import MaintenanceController

#id, maintenance_id, car_id, employee_id, service_type, cost)

class MaintenanceView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x350")
        self.window.title("Maintenance")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.maintenance_id = LabelWithEntry(self.window, "MaintenanceId", 20, 60, data_type=IntVar)
        self.car_id = LabelWithEntry(self.window, "CarId", 20, 100, data_type=IntVar)
        self.employee_id = LabelWithEntry(self.window, "EmployeeId", 20, 140, data_type=IntVar)
        self.service_type = LabelWithEntry(self.window, "ServiceType", 20, 180)
        self.cost = LabelWithEntry(self.window, "Cost", 20, 220, data_type=IntVar)

        self.table = Table(
            self.window,
            ["Id", "MaintenanceId", "CarId", "EmployeeId", "ServiceType", "Cost"],
            [40, 100, 100, 100, 100, 100],
            270, 20,
            14,
            self.select_from_table)


        Button(self.window, text="Select Maintenance", width=19, command=self.select_maintenance).place(x=20, y=260)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=260)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=300)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=300)
        self.reset_form()
        self.window.mainloop()

    # id, maintenance_id, car_id, employee_id, service_type, cost)

    def save_click(self):
        status, message = MaintenanceController.save(self.maintenance_id.get(), self.car_id.get(), self.employee_id.get(), self.service_type.get(),
                                             self.cost.get())
        if status:
            messagebox.showinfo("Maintenance Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Maintenance Save Error", message)

    def edit_click(self):
        status, message = MaintenanceController.update(self.id.get(), self.maintenance_id.get(), self.car_id.get(), self.employee_id.get(),
                                               self.service_type.get(), self.cost.get())
        if status:
            messagebox.showinfo("Maintenance Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Maintenance Update Error", message)

    def delete_click(self):
        status, message = MaintenanceController.delete(self.id.get())
        if status:
            messagebox.showinfo("Maintenance Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Maintenance Delete Error", message)


    def reset_form(self):
        self.id.set(0)
        self.maintenance_id.set(0)
        self.car_id.clear()
        self.employee_id.clear()
        self.service_type.clear()
        self.cost.clear()
        status, maintenance_list = MaintenanceController.find_all()
        self.table.refresh_table(maintenance_list)

    def select_from_table(self, selected_maintenance):
        if selected_maintenance:
            status, maintenance = MaintenanceController.find_by_id(selected_maintenance[0])
            if status:
                maintenance = Maintenance(*selected_maintenance)
                self.id.set(maintenance.id)
                self.maintenance_id.set(maintenance.maintenance_id)
                self.car_id.set(maintenance.car_id)
                self.employee_id.set(maintenance.employee_id)
                self.service_type.set(maintenance.service_type)
                self.cost.set(maintenance.cost)

    def select_maintenance(self):
        if self.id.get():
            status, Session.maintenance = MaintenanceController.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select Maintenance")

    def refresh(self):
        pass


if __name__ == "__main__":
    MaintenanceView()

