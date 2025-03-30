from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Skill, Experience
import numpy as np
import pandas as pd
import os
os.environ['MPLBACKEND'] = 'Agg'  # Set the backend environment variable
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg for web applications
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import seaborn as sns

def create_skill_radar_chart():
    # Create sample data for radar chart
    categories = ['Backend', 'Database', 'DevOps', 'Data Analysis', 'System Design', 'Problem Solving']
    values = [4.5, 4.2, 3.8, 4.0, 4.3, 4.7]
    
    # Compute angle for each category
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    
    # Close the plot by appending first value
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    categories = np.concatenate((categories, [categories[0]]))
    
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    # Plot data
    ax.plot(angles, values, 'o-', linewidth=2, label='Skills')
    ax.fill(angles, values, alpha=0.25)
    
    # Set labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories[:-1])
    
    # Add grid
    ax.grid(True)
    
    # Set title
    plt.title('Skills Radar Chart', pad=20)
    
    # Save to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close('all')
    return base64.b64encode(image_png).decode()

def create_learning_timeline():
    # Create fixed data for consistent timeline
    dates = pd.date_range(start='2020-01-01', end='2024-03-01', freq='ME')
    # Create a smooth, consistent curve
    x = np.linspace(0, 1, len(dates))
    skills = 0.5 + 0.5 * np.sin(x * np.pi) + 0.2 * x
    
    # Create figure with smaller size
    fig, ax = plt.subplots(figsize=(8, 4))  # Changed from (10, 6) to (8, 4)
    
    # Main timeline plot
    ax.plot(dates, skills, linewidth=2, color='#0d6efd')
    ax.fill_between(dates, skills, alpha=0.2, color='#0d6efd')
    
    # Add annotations for key milestones
    milestones = [
        ('2021-02-10', 'Started Python'),
        ('2021-03-10', 'Learned Django'),
        ('2022-01-01', 'Mastered Flask'),
        ('2023-01-01', 'Started Golang'),
        ('2024-01-01', 'Learning Rust')
    ]
    
    for date, text in milestones:
        date = pd.to_datetime(date)
        if date in dates:
            value = skills[dates.get_loc(date)]
            ax.annotate(text, (date, value), xytext=(10, 10), textcoords='offset points',
                        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    # Customize plot
    ax.set_title('Learning Journey Timeline', pad=20)
    ax.grid(True, alpha=0.3)
    
    # Save to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close('all')
    return base64.b64encode(image_png).decode()

def create_skill_distribution():
    # Create sample data
    np.random.seed(42)  # Fixed seed for consistency
    skills = ['Python', 'Django', 'Flask', 'Golang', 'Rust', 'PostgreSQL', 'SQLite']
    proficiency = np.random.normal(4, 0.5, len(skills))
    proficiency = np.clip(proficiency, 1, 5)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create violin plot
    sns.violinplot(y=skills, x=proficiency, ax=ax, color='#0d6efd', alpha=0.7)
    
    # Add individual points
    for i, skill in enumerate(skills):
        ax.scatter(proficiency[i], i, color='white', s=100, zorder=3)
        ax.text(proficiency[i], i, f'{proficiency[i]:.1f}', 
                ha='center', va='center', color='white', fontweight='bold')
    
    # Customize plot
    ax.set_title('Skill Distribution Analysis', pad=20)
    ax.set_xlabel('Proficiency Level')
    ax.set_ylabel('Technology')
    ax.grid(True, alpha=0.3)
    
    # Save to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close('all')
    return base64.b64encode(image_png).decode()

def home(request):
    # Get skills and calculate percentages
    skills = Skill.objects.all()
    for skill in skills:
        skill.percentage = skill.proficiency * 20
    
    # Create visualizations
    radar_chart = create_skill_radar_chart()
    distribution = create_skill_distribution()
    
    context = {
        'skills': skills,
        'experiences': Experience.objects.all()[:3],
        'radar_chart': radar_chart,
        'distribution': distribution,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_mail(
            f'Contact Form Message from {name}',
            f'From: {name}\nEmail: {email}\n\nMessage:\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        return render(request, 'core/contact.html', {'success': True})
    
    return render(request, 'core/contact.html')

def skills(request):
    skills_data = [
        # Backend Skills
        {"name": "Django", "category": "Backend Development", "proficiency": 5},
        {"name": "Flask", "category": "Backend Development", "proficiency": 4},
        {"name": "FastAPI", "category": "Backend Development", "proficiency": 4},
        # Database Skills
        {"name": "PostgreSQL", "category": "Database Management", "proficiency": 5},
        {"name": "MongoDB", "category": "Database Management", "proficiency": 4},
        {"name": "Redis", "category": "Database Management", "proficiency": 3},
        # Other Skills
        {"name": "Git", "category": "Other Skills", "proficiency": 5},
        {"name": "Docker", "category": "Other Skills", "proficiency": 4},
        {"name": "AWS", "category": "Other Skills", "proficiency": 4},
    ]

    # Process skills data
    for skill in skills_data:
        skill["percentage"] = skill["proficiency"] * 20
        skill["level_text"] = get_proficiency_text(skill["proficiency"])
        skill["category_display"] = skill["category"]

    # Group skills by category
    skills_by_category = {}
    for skill in skills_data:
        category = skill["category"]
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)

    return render(request, "core/skills.html", {"skills_by_category": skills_by_category})

def get_proficiency_text(level):
    return {
        1: "Beginner",
        2: "Intermediate",
        3: "Advanced",
        4: "Expert",
        5: "Master"
    }.get(level, "Unknown")

def experience(request):
    experiences = [
        {
            'title': 'Freelancer',
        },
        # Add more experiences as needed
    ]
    return render(request, 'core/experience.html', {'experiences': experiences})
