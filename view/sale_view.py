from view import *
from model import Sale, Session
from controller import SaleController


class SaleView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("980x370")
        self.window.title("Sale")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.sale_id = LabelWithEntry(self.window, "SaleId", 20, 60, data_type=IntVar)
        self.car_id = LabelWithEntry(self.window, "CarId", 20, 100, data_type=IntVar)
        self.customer_id = LabelWithEntry(self.window, "CustomerId", 20, 140, data_type=IntVar)
        self.employee_id = LabelWithEntry(self.window, "EmployeeId", 20, 180, data_type=IntVar)
        self.date_time = LabelWithEntry(self.window, "DateTime", 20, 220)
        self.final_cost = LabelWithEntry(self.window, "FinalCost", 20, 260, data_type=IntVar)

        self.table = Table(
            self.window,
            ["Id", "SaleId", "CarId", "CustomerId", "EmployeeId", "DateTime", "FinalCost"],
            [40, 100, 100, 100, 100, 130, 100],
            270, 20,
            15,
            self.select_from_table
        )

        Button(self.window, text="Select Sale", width=19, command=self.select_sale).place(x=20, y=290)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=290)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=330)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=330)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=330)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = SaleController.save(self.sale_id.get(), self.car_id.get(), self.customer_id.get(),
                                              self.employee_id.get(),
                                              self.date_time.get(), self.final_cost.get())
        if status:
            messagebox.showinfo("Sale Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Sale Save Error", message)

    def edit_click(self):
        status, message = SaleController.update(self.id.get(), self.sale_id.get(), self.car_id.get(),
                                                self.customer_id.get(), self.employee_id.get(),
                                                self.date_time.get(), self.final_cost.get())
        if status:
            messagebox.showinfo("Sale Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Sale Update Error", message)

    def delete_click(self):
        status, message = SaleController.delete(self.id.get())
        if status:
            messagebox.showinfo("Sale Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Sale Delete Error", message)

    def reset_form(self):
        self.id.set(0)
        self.sale_id.set(0)
        self.car_id.clear()
        self.customer_id.clear()
        self.employee_id.clear()
        self.date_time.clear()
        self.final_cost.clear()
        status, sale_list = SaleController.find_all()
        self.table.refresh_table(sale_list)

    def select_from_table(self, selected_sale):
        if selected_sale:
            status, customer = SaleController.find_by_id(selected_sale[0])
            if status:
                sale = Sale(*selected_sale)
                self.id.set(sale.id)
                self.sale_id.set(sale.sale_id)
                self.car_id.set(sale.car_id)
                self.customer_id.set(sale.customer_id)
                self.employee_id.set(sale.employee_id)
                self.date_time.set(sale.date_time)
                self.final_cost.set(sale.final_cost)

    def select_sale(self):
        if self.id.get():
            status, Session.sale = SaleController.find_by_id(self.id.get())
        else:
            messagebox.showerror("Select", "Select Sale")

    def refresh(self):
        self.reset_form()
