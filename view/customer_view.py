from view import *
from model import Customer, Session
from controller import CustomerController

class CustomerView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("900x350")
        self.window.title("Customer")

        self.id= LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.customer_id = LabelWithEntry(self.window, "CustomerId", 20, 60, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 100)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 140)
        self.mobile_number = LabelWithEntry(self.window, "MobileNumber", 20, 180)
        self.address = LabelWithEntry(self.window, "Address", 20, 220)


        self.table = Table(
            self.window,
            ["Id", "customer_id", "first_name", "last_name", "mobile_number", "address"],
            [40, 100, 100, 100, 100, 160],
            275, 20,
            14,
            self.select_from_table
        )

        Button(self.window, text="Select Customer", width=19, command=self.select_customer).place(x=20, y=260)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=260)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=300)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=300)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = CustomerController.save(self.customer_id.get(), self.first_name.get(), self.last_name.get(), self.mobile_number.get(),
                                                  self.address.get())

        if status:
            messagebox.showinfo("Customer Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Save Error", message)

    def edit_click(self):
        status, message = CustomerController.update(self.id.get(), self.customer_id.get(), self.first_name.get(), self.last_name.get(),
                                               self.mobile_number.get(), self.address.get())
        if status:
            messagebox.showinfo("Customer Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Update Error", message)

    def delete_click(self):
        status, message = CustomerController.delete(self.id.get())
        if status:
            messagebox.showinfo("Customer Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Delete Error", message)

    def reset_form(self):
            self.id.set(0)
            self.customer_id.set(0)
            self.first_name.clear()
            self.last_name.clear()
            self.mobile_number.clear()
            self.address.clear()
            status, customer_list = CustomerController.find_all()
            self.table.refresh_table(customer_list)


    def select_from_table(self, selected_customer):
            if selected_customer:
                status, customer = CustomerController.find_by_id(selected_customer[0])
                if status:
                    customer = Customer(*selected_customer)
                    self.id.set(customer.id)
                    self.customer_id.set(customer.customer_id)
                    self.first_name.set(customer.first_name)
                    self.last_name.set(customer.last_name)
                    self.mobile_number.set(customer.mobile_number)
                    self.address.set(customer.address)

    def select_customer(self):
            if self.id.get():
                status, Session.bank = CustomerController.find_by_id(self.id.get())
            else:
                messagebox.showerror("Select", "Select Customer")

    def refresh(self):
            pass



if __name__ == "__main__":
        CustomerView()