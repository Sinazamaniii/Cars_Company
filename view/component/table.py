from tkinter import *
import tkinter.ttk as ttk


class Table:
    def table_select(self, event):
        row_id = self.table.focus()
        item = self.table.item(row_id)["values"]
        self.function_name(item)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def refresh_table(self, data_list):
        self.clear_table()
        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data.to_tuple())