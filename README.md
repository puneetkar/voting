Voting System

A simple full-stack voting system built with Django, HTML, CSS, and JavaScript. Users can vote for two candidates (V1 and V2), and the system displays real-time voting results.

Features

User-friendly voting interface

Django backend for handling votes

Database storage for votes

Real-time results with Fetch API

Secure API for vote submission

Technologies Used

Frontend: HTML, CSS, JavaScript (Fetch API)

Backend: Django (Python)

Database: SQLite (default) or PostgreSQL/MySQL (optional)

Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/voting-system.git
cd voting-system

2️⃣ Install Dependencies

pip install django

3️⃣ Start Django Project & App

django-admin startproject voting_project
cd voting_project
python manage.py startapp voting_app

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Server

python manage.py runserver

6️⃣ Open in Browser

Visit http://127.0.0.1:8000/ to start voting!

Project Structure

voting_project/
│── voting_app/
│   ├── migrations/
│   ├── static/       # CSS file (style.css)
│   ├── templates/    # HTML file (index.html)
│   │   ├── index.html
│   ├── views.py      # Handles voting logic
│   ├── urls.py       # API routes
│   ├── models.py     # Vote database model
│── voting_project/
│   ├── settings.py
│   ├── urls.py
│── manage.py

API Endpoints

Method

Endpoint

Description

GET

/

Renders the voting page

POST

/vote/

Casts a vote for V1 or V2

GET

/results/

Fetches vote counts

Future Enhancements

✅ User authentication (Login & Registration)

✅ Prevent duplicate voting

✅ Admin dashboard for vote monitoring
