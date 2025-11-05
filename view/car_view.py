from view import *
from model import Car, Session
from controller import CarController


class CarView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("750x320")
        self.window.title("Car")

        self.car_id = LabelWithEntry(self.window, "Id", 20,20, data_type=IntVar, state="readonly")
        self.brand= LabelWithEntry(self.window, "Brand", 20,60)
        self.model= LabelWithEntry(self.window, "Model", 20,100)
        self.year = LabelWithEntry(self.window, "Year", 20,140,data_type= IntVar)
        self.price= LabelWithEntry(self.window, "Price", 20,180)

        self.table = Table(
            self.window,
            ["Id", "Brand", "Model", "Year", "Price"],
            [40, 100, 100, 60, 150],
            270, 20,
            12,
            self.select_from_table
        )




        Button(self.window, text="Select Car", width=19, command=self.select_car).place(x=20, y=220)
        Button(self.window, text="Refresh", width=7, command=self.refresh).place(x=180, y=220)
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)
        self.reset_form()
        self.window.mainloop()


    def save_click(self):
        status, message= CarController.save(self.brand.get(), self.model.get(), self.year.get(), self.price.get())
        if status:
            messagebox.showinfo("Car Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Car Save Error", message)

    def edit_click(self):
        status, message= CarController.update(self.car_id.get(), self.brand.get(), self.model.get(), self.year.get(), self.price.get())
        if status:
            messagebox.showinfo("Car Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Car Update Error", message)

    def delete_click(self):
        status, message= CarController.delete(self.car_id.get())
        if status:
            messagebox.showinfo("Car Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Car Delete Error", message)

    def reset_form(self):
        self.car_id.clear()
        self.brand.clear()
        self.model.clear()
        self.year.clear()
        self.price.clear()
        status, car_list = CarController.find_all()
        self.table.refresh_table(car_list)

    def select_from_table(self, selected_car):
        if selected_car:
            status, car = CarController.find_by_id(selected_car[0])
            if status:
                car = Car(*selected_car)
                self.car_id.set(car.car_id)
                self.brand.set(car.brand)
                self.model.set(car.model)
                self.year.set(car.year)
                self.price.set(car.price)

    def select_car(self):
        if self.car_id.get():
            status, Session.bank = CarController.find_by_id(self.car_id.get())
        else:
            messagebox.showerror("Select", "Select Bank")

    def refresh(self):
        pass


