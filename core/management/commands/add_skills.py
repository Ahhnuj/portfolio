from django.core.management.base import BaseCommand
from core.models import Skill

class Command(BaseCommand):
    help = 'Adds initial skills to the database'

    def handle(self, *args, **kwargs):
        # Backend Skills
        backend_skills = [
            {'name': 'Django', 'proficiency': 5, 'category': 'backend'},
            {'name': 'Flask', 'proficiency': 4, 'category': 'backend'},
            {'name': 'Python', 'proficiency': 5, 'category': 'backend'},
            {'name': 'Golang', 'proficiency': 3, 'category': 'backend'},
            {'name': 'Rust', 'proficiency': 2, 'category': 'backend'},
        ]

        # Database Skills
        database_skills = [
            {'name': 'PostgreSQL', 'proficiency': 4, 'category': 'database'},
            {'name': 'SQLite', 'proficiency': 5, 'category': 'database'},
            {'name': 'Database Design', 'proficiency': 4, 'category': 'database'},
        ]

        # Other Skills
        other_skills = [
            {'name': 'Git', 'proficiency': 4, 'category': 'other'},
            {'name': 'Docker', 'proficiency': 3, 'category': 'other'},
            {'name': 'REST APIs', 'proficiency': 4, 'category': 'other'},
        ]

        # Add all skills
        for skill_data in backend_skills + database_skills + other_skills:
            Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'proficiency': skill_data['proficiency'],
                    'category': skill_data['category']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added skills')) 