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

git clone https://github.com/<your-username>/Cars_Company.git
cd Cars_Company

---

## 🖥️ Run Application

# 1️⃣ Navigate to your project folder
cd Cars_Company

# 2️⃣ Run the main entry point
python app.py

---

## 🧠 Project Structure

Cars_Company/
│
├── app.py                      # Entry point to run the whole application
│
├── controller/                 # Handles all business logic and coordination
│   ├── __init__.py
│   ├── employee_controller.py
│   ├── car_controller.py
│   ├── customer_controller.py
│   ├── maintenance_controller.py
│   └── sale_controller.py
│
├── model/                      # Database models and logic
│   ├── __init__.py
│   ├── employee.py
│   ├── car.py
│   ├── customer.py
│   ├── maintenance.py
│   ├── sale.py
│   ├── session.py              # Holds logged-in user session
│   └── repositories/           # SQLite repositories
│       ├── employee_repository.py
│       ├── car_repository.py
│       ├── customer_repository.py
│       ├── maintenance_repository.py
│       └── sale_repository.py
│
├── view/                       # User interface (Tkinter-based)
│   ├── __init__.py
│   ├── dashboard_view.py       # Central dashboard
│   ├── login_view.py           # Login & guest mode
│   ├── car_view.py
│   ├── customer_view.py
│   ├── employee_view.py
│   ├── maintenance_view.py
│   ├── sale_view.py
│   ├── component/              # Shared UI widgets
│   │   ├── table.py
│   │   └── label_with_entry.py
│   └── images/                 # App icons and logos
│       ├── logo.png
│       └── user.png
│
└── db/
    └── cars_co_db.db           # SQLite database file
