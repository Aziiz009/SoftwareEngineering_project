import os
import pytest
import importlib.util

# --- Correct project root (Desktop/syed) ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
APP_PATH = os.path.join(PROJECT_ROOT, "app.py")

# Load app.py manually
spec = importlib.util.spec_from_file_location("app", APP_PATH)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)

app = app_module.app
db = app_module.db
User = app_module.User
Student = app_module.Student


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


def test_home_redirect(client):
    res = client.get("/")
    assert res.status_code == 302   # redirect to login


def test_login(client):
    res = client.post(
        "/login",
        data={
            "username": "teacher",
            "password": "teacher123"
        },
        follow_redirects=True
    )

    assert b"Attendance" in res.data


def test_students_exist():
    with app.app_context():
        students = Student.query.all()
        assert len(students) > 0
