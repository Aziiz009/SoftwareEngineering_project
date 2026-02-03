Great — now we add the most important academic document:


# 🧱 System Architecture – Attendance Management System

## 1. Architecture Overview

The Attendance Management System is a **web-based client–server application** developed using the **Flask framework**.
It follows a **Model–View–Controller (MVC)** style architecture.

The system consists of:

* A web browser interface (user interface)
* A Flask backend (application logic)
* A SQLite database (data storage)

---

## 2. High-Level Architecture

```
[ User (Browser) ]
        |
        v
[ HTML Templates ]
        |
        v
[ Flask Controllers ]
        |
        v
[ Business Logic ]
        |
        v
[ SQLAlchemy ORM ]
        |
        v
[ SQLite Database ]
```

---

## 3. Main Components

### 3.1 User Interface (View)

The UI is created using HTML templates:

* `login.html` – for user authentication
* `index.html` – for attendance management

The browser sends requests to the Flask server and displays the responses.

---

### 3.2 Application Layer (Controller)

The Flask application (`app.py`) controls:

* Login and logout
* Attendance submission
* Access control using user roles

Flask routes handle user requests and connect them to the business logic.

---

### 3.3 Data Layer (Model)

The system uses **SQLAlchemy ORM** to manage database tables:

| Table      | Purpose                            |
| ---------- | ---------------------------------- |
| User       | Stores login credentials and roles |
| Student    | Stores student data                |
| Attendance | Stores attendance records          |

These models allow the system to store data permanently in SQLite.

---

### 3.4 Authentication and Security

The system uses:

* **Flask-Login** for session management
* **Werkzeug password hashing** for secure password storage

Only authenticated users can access the attendance system.
Only teachers are allowed to mark attendance.

---

## 4. Why These Technologies Were Chosen

| Technology  | Reason                             |
| ----------- | ---------------------------------- |
| Flask       | Lightweight and easy to use        |
| SQLite      | Simple and reliable local database |
| SQLAlchemy  | Simplifies database operations     |
| Flask-Login | Provides secure authentication     |
| Pytest      | Enables automated testing          |

---

## 5. Non-Functional Requirements

The architecture supports:

* **Security** – passwords are hashed
* **Reliability** – data stored in a database
* **Maintainability** – clear separation of components
* **Scalability** – can be extended with more features

---

## 6. Conclusion

The architecture ensures that the system is structured, secure, and easy to maintain.
It follows standard web application design principles.

