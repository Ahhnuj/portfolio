from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Project
from .forms import ProjectForm
from taggit.models import Tag

def project_list(request, tag_slug=None):
    projects = Project.objects.all()
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        projects = projects.filter(technologies__in=[tag])
    
    search_query = request.GET.get('search')
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    paginator = Paginator(projects, 6)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    
    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'tag': tag_slug,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            form.save_m2m()  # Save tags
            messages.success(request, 'Project added successfully!')
            return redirect('projects:project_detail', slug=project.slug)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form, 'action': 'New'})

@login_required
def project_edit(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            form.save_m2m()  # Save tags
            messages.success(request, 'Project updated successfully!')
            return redirect('projects:project_detail', slug=project.slug)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'action': 'Edit'})

@login_required
def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects:project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})
