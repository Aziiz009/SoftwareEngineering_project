from flask import Flask, render_template, jsonify, request, redirect, url_for
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os

# -------------------------
# Flask App Configuration
# -------------------------
app = Flask(__name__)
app.secret_key = "supersecretkey"   # required for sessions

# Force Flask to use project folder instead of /instance
app.instance_path = os.path.abspath(os.path.dirname(__file__))

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------
# Login Manager
# -------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# -------------------------
# Database Models
# -------------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # teacher / student


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -------------------------
# Initial Data
# -------------------------
registered_students = ["Thomas", "James", "Aziz", "Jordan", "Charles"]

# -------------------------
# Routes
# -------------------------
@app.route("/")
@login_required
def home():
    students = Student.query.all()
    student_list = [{"id": s.id, "name": s.name} for s in students]
    return render_template("index.html", students=student_list, role=current_user.role)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("home"))

        return "Invalid credentials"

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/mark", methods=["POST"])
@login_required
def mark_attendance():
    if current_user.role != "teacher":
        return jsonify({"status": "error", "message": "Only teachers can mark attendance"}), 403

    data = request.get_json()
    name = data.get("name", "").strip().title()

    if not name:
        return jsonify({"status": "error", "message": "No name provided"}), 400

    student = Student.query.filter_by(name=name).first()
    if not student:
        return jsonify({"status": "error", "message": "Student not found"}), 404

    today = date.today()
    already = Attendance.query.filter_by(student_id=student.id, date=today).first()
    if already:
        return jsonify({"status": "error", "message": f"{name} already marked today"}), 400

    record = Attendance(student_id=student.id, date=today, status="Present")
    db.session.add(record)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": f"{name} marked present",
        "record": {
            "name": name,
            "date": today.strftime("%d/%m/%Y"),
            "status": "Present"
        }
    })

# -------------------------
# Database Setup
# -------------------------
with app.app_context():
    db.create_all()

    # Seed students
    if Student.query.count() == 0:
        for s in registered_students:
            db.session.add(Student(name=s))
        db.session.commit()

    # Create default teacher
    if User.query.count() == 0:
        teacher = User(
            username="teacher",
            password=generate_password_hash("teacher123", method="pbkdf2:sha256"),
            role="teacher"
        )
        db.session.add(teacher)
        db.session.commit()

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
