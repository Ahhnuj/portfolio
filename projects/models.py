from django.db import models
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-featured', '-created_at', 'order']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.slug])
    
    def get_technologies_list(self):
        return [tag.name for tag in self.technologies.all()]
