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

git clone [https://github.com/<your-username>/Cars_Company.git](https://github.com/Sinazamaniii/Cars_Company)

---

## 🖥️ Run Application

# 1️⃣ Navigate to your project folder
Cars_Company

# 2️⃣ Run the main entry point
python app.py

---

## 🧠 Project Structure

```bash

Cars_Company/
│
├── app.py # Entry point to start the entire application
│
├── model/ # Data entities (core domain models)
│ ├── init.py
│ ├── car.py # Car entity
│ ├── customer.py # Customer entity
│ ├── employee.py # Employee entity
│ ├── maintenance.py # Maintenance entity
│ ├── sale.py # Sale entity
│ └── session.py # Tracks logged-in employee (active session)
│
├── repository/ # Database operations (CRUD for each entity)
│ ├── init.py
│ ├── car_repository.py
│ ├── customer_repository.py
│ ├── employee_repository.py
│ ├── maintenance_repository.py
│ └── sale_repository.py
│
├── service/ # Business logic layer (between controller and repo)
│ ├── init.py
│ ├── car_service.py
│ ├── customer_service.py
│ ├── employee_service.py
│ ├── maintenance_service.py
│ └── sale_service.py
│
├── controller/ # Coordinates view actions and service calls
│ ├── init.py
│ ├── car_controller.py
│ ├── customer_controller.py
│ ├── employee_controller.py
│ ├── maintenance_controller.py
│ └── sale_controller.py
│
├── tools/ # Input validators and shared utilities
│ ├── init.py
│ ├── customer_validator.py
│ ├── employee_validator.py
│ ├── car_validator.py
│ ├── maintenance_validator.py
│ └── sale_validator.py
│
├── view/ # Tkinter GUI (presentation layer)
│ ├── init.py
│ ├── dashboard_view.py # Main dashboard (central navigation)
│ ├── login_view.py # Login and guest mode
│ ├── car_view.py # Car management UI
│ ├── customer_view.py # Customer management UI
│ ├── employee_view.py # Employee management UI
│ ├── maintenance_view.py # Maintenance management UI
│ ├── sale_view.py # Sales management UI
│ │
│ ├── component/ # Reusable UI elements
│ │ ├── init.py
│ │ ├── label_with_entry.py # Custom Label+Entry widget
│ │ └── table.py # Custom table display
│ │
│ └── images/ # App visuals and icons
│ ├── logo.png
│ └── user.png
│
├── test/ # Unit and integration tests
│ ├── init.py
│ ├── customer_test.py
│ ├── employee_test.py
│ ├── car_test.py
│ ├── maintenance_test.py
│ └── sale_test.py
│
└── db/
└── cars_co_db.db # SQLite database file
