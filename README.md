# Anuj Tiwari's Portfolio Website

A personal portfolio website showcasing my skills, projects, and journey as a backend developer. Built with Django and featuring interactive elements.

## Features

- Dynamic portfolio showcasing projects and skills
- Interactive career progress visualization
- Blog section for sharing thoughts and experiences
- Professional yet engaging design
- Responsive layout for all devices
- Contact information and social links

## Tech Stack

- Django 5.0.2
- Bootstrap 5
- NumPy & Pandas for data visualization
- Matplotlib for graphs
- SQLite/PostgreSQL database

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the website.

## Project Structure

- `portfolio/` - Main project directory
- `core/` - Core application with main views and models
- `blog/` - Blog application for posts
- `projects/` - Projects showcase application
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates 