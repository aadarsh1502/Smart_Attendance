📘 Smart Attendance Management System

A role-based attendance management web application built using Django that allows faculty to mark attendance and students to track their attendance percentage across multiple subjects.

🚀 Features
👨‍🏫 Faculty

Login using Django authentication

View assigned subjects

Mark attendance using checkbox system

Automatically marks unchecked students as Absent

Prevents duplicate attendance for the same day

👨‍🎓 Student

Login using Django authentication

View subject-wise attendance

View:

Total classes attended

Total classes conducted

Percentage per subject

Overall attendance percentage

🛠 Admin

Add Students

Add Faculty

Add Subjects

Manage Users via Django Admin Panel

🏗 Tech Stack

Python

Django

SQLite

HTML

Bootstrap

Django Admin

Django Authentication System

🗂 Database Design
Models Used:
1️⃣ Faculty

OneToOne relationship with Django User

Stores employee ID

2️⃣ Student

OneToOne relationship with Django User

Registration number

Roll number

Parent email

3️⃣ Subject

Linked to Faculty (ForeignKey)

4️⃣ Attendance

Linked to:

Student (ForeignKey)

Subject (ForeignKey)

Faculty (marked_by)

Stores:

Date

Status (Present / Absent)

Prevents duplicate attendance using:

unique_together = ('student', 'subject', 'date')
🧠 Core Logic
✅ Attendance Marking

Uses:

Attendance.objects.update_or_create()

Updates if attendance exists

Creates if not exists

Automatically assigns Absent to unchecked students

📊 Attendance Calculation

For each subject:

percentage = (present_classes / total_classes) * 100

Also calculates overall attendance across all subjects.

🔐 Role-Based Dashboard

The system checks:

If superuser → redirect to admin panel

If Faculty → faculty dashboard

If Student → student dashboard

🛠 Installation
git clone <your-repo-link>
cd Smart_Attendance
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
📌 Future Improvements

Subject-wise student filtering

Email alerts for low attendance

Attendance analytics dashboard

CSV export feature

Role-based access control improvement

📚 What I Learned

Django ORM relationships

OneToOne vs ForeignKey usage

Role-based authentication

Aggregation logic in Django

update_or_create() method

unique_together constraint

Clean dashboard rendering

Building full-stack project from scratch

💡 Project Status

Completed (Basic Version)
Future upgrades planned.
