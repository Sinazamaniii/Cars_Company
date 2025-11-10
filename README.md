# 🚗 Cars Company Management System

A desktop management system built with **Python (Tkinter + SQLite)** that helps car dealerships manage their operations — from handling cars and customers to tracking sales, maintenance, and employee activity.  
It’s designed for simplicity, structure, and learning: a modular application following the **MVC (Model–View–Controller)** pattern for clean separation between logic, interface, and data.

---

## 📘 Overview

The **Cars Company Management System** provides a graphical interface for managing every aspect of a car dealership.  
Employees can log in and access all system features, while guests can open the dashboard in a restricted mode that hides private details (like customer addresses and internal data).

Each module (Cars, Customers, Employees, Maintenance, Sales) is implemented as a separate *View*, connected to its own *Controller* and *Model* for clear, maintainable organization.

---

## ⚙️ Features

✅ **Login System**  
- Employee authentication with username and password  
- Optional guest access with limited functionality  
- In-memory session handling (via `Session.employee`)  

✅ **Dashboard**  
- Central hub with navigation to all views  
- Displays company logo and logged-in user  
- Certain sections auto-lock when accessed as a guest  

✅ **Customer Management**  
- Add, edit, and delete customer data  
- Addresses hidden in guest mode for privacy  
- Live data table with refresh functionality  

✅ **Car Management**  
- Store, update, and remove car listings  
- View details about available vehicles  

✅ **Employee Management**  
- Manage employee records, login details, and roles  

✅ **Maintenance Records**  
- Log service history, repairs, and maintenance costs  

✅ **Sales Records**  
- Record completed sales, linked to customers and employees  

---

## 🧩 Tech Stack

- **Python 3.x**
- **Tkinter** → GUI framework  
- **SQLite3** → Local database  
- **Pillow (PIL)** → Image rendering  
- **MVC Pattern** → Clear separation of concerns  

---

## 🖥️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Cars_Company.git
cd Cars_Company
