from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

from .models import Project, Milestone, Task, Document, Document
from company_management.models import Company
from .forms import ProjectForm, MilestoneForm, TaskForm, DocumentForm

# Create your views here.
def ongoingProjects(request):
    return render(request, 'project_management/ongoingprojects.html')

def listOfIncidents(request):
    return render(request, 'project_management/incidents.html')

def listOfMilesoneIncidents(request):
    return render(request, 'project_management/milestoneincidents.html')

def listOfTaskIncidents(request):
    return render(request, 'project_management/taskincidents.html')

def incident(request):
    return render(request, 'project_management/incident.html')

def newIncident(request):
    return render(request, 'project_management/newincident.html')

def previousProjects(request):
    return render(request, 'project_management/previousprojects.html')

def newProject(request):
    return render(request, 'project_management/newproject.html')


# Custom Views
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['ongoing_projects_list'] = Project.objects.all().filter(project_status='New')
        return context

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = DocumentForm()
    return render(request, 'project_management/model_form_upload.html', {
        'form': form
    })

def load_project_documents(request):
    project_id = request.GET.get('project')
    #documents = Document.objects.filter(project_id=project_id).order_by('name')
    documents = Document.objects.all
    return render(request, 'project_management/document_dropdown_list_options.html', {'documents': documents})

class ProjectDetailView(DetailView):
    model = Project
    #form_class = ProjectForm
    success_url = reverse_lazy('project_list')

class CompleteProjectListView(ListView):
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['ongoing_projects_list'] = Project.objects.all().filter(project_status='Completed')
        return context


class TerminatedProjectListView(ListView):
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['ongoing_projects_list'] = Project.objects.all().filter(project_status=2)
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

#Milestone
class MilestoneCreateView(CreateView):
    model = Milestone
    form_class = MilestoneForm
    success_url = reverse_lazy('milestone_list')

class MilestoneListView(ListView):
    model = Milestone
    context_object_name = 'milestones'

def load_milestones(request):
    #project_id = request.GET.get('project')
    #milestones = Milestone.objects.filter(project_id=project_id).order_by('name')
    projects = Project.objects.all
    return render(request, 'project_management/milestone_list.extended.html', {'projects': projects})

def load_task_milestoneI_list(request):
    project_id = request.GET.get('project')
    milestones = Milestone.objects.filter(project_id=project_id).order_by('name')
    return render(request, 'project_management/new_task_milestone_dropdown_list_options.html', {'milestones': milestones})

class MilestoneUpdateView(UpdateView):
    model = Milestone
    form_class = MilestoneForm
    success_url = reverse_lazy('milestone_list')

#Task
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

def load_task_milestones(request):
    project_id = request.GET.get('project')
    milestones = Milestone.objects.filter(project_id=project_id).order_by('name')
    return render(request, 'project_management/task_milestone_dropdown_list_options.html', {'milestones': milestones})