from view import *
from model import Employee, Session
from controller import EmployeeController


class EmployeeView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Employee")
        self.window.geometry("950x400")

        # id, employee_id, first_name, last_name, occupation, username, password)

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.employee_id = LabelWithEntry(self.window, "EmployeeId", 20, 60, data_type=IntVar)
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 100)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 140)
        self.occupation = LabelWithEntry(self.window, "Occupation", 20, 180)
        self.username = LabelWithEntry(self.window, "Username", 20, 220)
        self.password = LabelWithEntry(self.window, "Password", 20, 260)

        self.table = Table(self.window,
                           ["Id", "EmployeeId", "FirstName", "LastName", "Occupation", "Username", "Password"],
                           [40, 100, 100, 100, 100, 100, 100, 100],
                           270, 20,
                           16,
                           self.select_from_table)

        Button(self.window, text="Select Employee", width=19, command=self.select_employee).place(x=20, y=300)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=300)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = EmployeeController.save(self.employee_id.get(), self.first_name.get(), self.last_name.get(),
                                                  self.occupation.get(), self.username.get(), self.password.get())
        if status:
            messagebox.showinfo("Employee Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Save Error", message)

    def edit_click(self):
        status, message = EmployeeController.update(self.id.get(), self.employee_id.get(), self.first_name.get(),
                                                    self.last_name.get(), self.occupation.get(), self.username.get(),
                                                    self.password.get())
        if status:
            messagebox.showinfo("Employee Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Update Error", message)

    def delete_click(self):
        status, message = EmployeeController.delete(self.id.get())
        if status:
            messagebox.showinfo("Employee Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Delete Error", message)

    def reset_form(self):
        self.id.set(0)
        self.employee_id.set(0)
        self.first_name.clear()
        self.last_name.clear()
        self.occupation.clear()
        self.username.clear()
        self.password.clear()
        status, employee_list = EmployeeController.find_all()
        self.table.refresh_table(employee_list)

    def select_from_table(self, selected_employee):
        if selected_employee:
            status, employee = EmployeeController.find_by_id(selected_employee[0])
            if status:
                employee = Employee(*selected_employee)
                self.id.set(employee.id)
                self.employee_id.set(employee.employee_id)
                self.first_name.set(employee.first_name)
                self.last_name.set(employee.last_name)
                self.occupation.set(employee.occupation)
                self.username.set(employee.username)
                self.password.set(employee.password)

    def select_employee(self):
        if self.id.get():
            status, Session.employee = EmployeeController.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select Employee")

    def refresh(self):
        pass

# if __name__ == "__main__":
# EmployeeView()
