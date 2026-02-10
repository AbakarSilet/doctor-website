# Doctor Website – Django Project

Professional medical website and blog built with Django.

This project includes a multilingual medical blog and a professional portfolio
for a doctor based in Africa, with a strong focus on SEO, performance and clean architecture.

## Features
- Django backend
- Blog system with SEO-friendly URLs
- Multilingual support (French / English / Arabic)
- Internationalized templates (i18n)
- Portfolio & contact pages
- Environment variables for security
- Ready for Dockerization

## Tech Stack
- Python
- Django
- HTML / CSS
- JavaScript
- PostgreSQL 

## Project Structure
lekmya blog/
│
├── manage.py
├── lekamyablog/        
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/           
├── blog/              
├── locale/             
├── templates/
├── static/
├── requirements.txt
├── .env                ← non commité
└── README.md

## Installation (Local)
``bash
git clone https://github.com/AbakarSilet/doctor-website.git
cd doctor-website
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
