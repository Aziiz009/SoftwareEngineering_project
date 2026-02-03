 🧪 Testing – Attendance Management System

# 1. Purpose of Testing

Testing checks if the Attendance Management System does what it's supposed to do. Its main job is making sure the system runs right and follows every needed step.

From the start, test cases built with Pytest checked things closely - not just once but repeatedly, making sure each part worked as expected without being rushed.

* The application starts correctly
* Login works as expected
Student details sit inside the database system.


# 2. Testing Framework

The project uses:

| Tool              | Purpose                     |
| ----------------- | --------------------------- |
| Pytest            | Automated testing framework |
| Flask Test Client | Simulates browser requests  |

These tools allow testing the system without using a real browser.


# 3. Test Cases

A file named `tests/test_app.py`, built to run checks without human help. Its job? To test things automatically.

The following tests are implemented:

# Test 1 – Home page protection

When someone visits without logging in, they get sent straight to the login screen instead of staying where they were.

# Test 2 – Login functionality

Every time, logging in should work for the built-in teacher account.

# Test 3 – Student data

Before proceeding, the system verifies whether each student is recorded in the database.

# 4. How to Run Tests

Start the terminal inside your project directory. Then execute

Run it by typing python3 -m pytest

When every check succeeds, then things are running right.

# 5. Test Results

The test execution shows -

3 passed

This shows the system works like it should.

# 6. Conclusion

Testing without people makes systems more trustworthy while protecting new updates from ruining what already works.