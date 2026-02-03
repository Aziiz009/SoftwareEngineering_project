1. Project Overview
This project is a web-based Attendance Management System developed using Flask (Python) and SQLite.It allows a teacher to log in and manage student attendance in a simple and secure way.
The system is designed for small educational institutions such as colleges, training centers, or private classes.

2. Features
* Secure login system for teachers
* Student database stored in SQLite
* Automatic creation of a default teacher account
* Attendance marking interface
* Protected pages (only logged-in users can access them)
* Automated testing using Pytest

3. Technologies Used
Technology	Purpose
Python	Backend programming
Flask	Web framework
Flask-SQLAlchemy	Database ORM
Flask-Login	Authentication
SQLite	Database
HTML	Web interface
Pytest	Automated testing
4. Folder Structure

syed/
 ├── app.py
 ├── attendance.db
 ├── static/
 ├── templates/
 │    ├── login.html
 │    └── index.html
 └── tests/
      └── test_app.py

5. Default Login Credentials
The system automatically creates a default teacher account:

Username: teacher
Password: teacher123

6. How to Run the Application
Step 1 – Install required packages
Open Terminal and run:

pip install flask flask-sqlalchemy flask-login werkzeug pytest

Step 2 – Run the Flask application
Navigate to the project folder:

cd Desktop/syed
Run the application:

python3 app.py
Open browser and go to:

http://127.0.0.1:5000/login

7. How to Run Tests
Inside the syed folder, run:

python3 -m pytest
You should see output similar to:

3 passed
This confirms the system is working correctly.

8. Purpose of Testing
The tests verify that:
* The login page is protected
* A teacher can log in
* Students exist in the database
This ensures system reliability.

9. Conclusion
This Attendance Management System provides a simple and effective way to manage student attendance using modern web technologies and automated testing.
