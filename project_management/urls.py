from django.urls import path
from . import views

#urls
urlpatterns = [
    path('ongoingProjects/', views.ongoingProjects, name='ongoingProjects'),
    path('incidents/', views.listOfIncidents, name='incidents'),
    path('milestoneIncidents/', views.listOfMilesoneIncidents, name='milestoneIncidents'),
    path('taskIncidents/', views.listOfTaskIncidents, name='taskIncidents'),
    path('incident/', views.incident, name='incident'),
    path('newincident/', views.newIncident, name='newIncident'),
    path('previousProjects/', views.previousProjects, name='previousProjects'),
    path('newProject/', views.newProject, name='newProject'),
    #new urls
    path('ongoing/', views.ProjectListView.as_view(), name='project_list'),
    path('projectdoc', views.model_form_upload, name='model_form_upload'),
    path('projectdocs/', views.load_project_documents, name='projectdocs_list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_details'),
    path('complete/', views.CompleteProjectListView.as_view(), name='complete_project_list'),
    path('terminated/', views.TerminatedProjectListView.as_view(), name='terminated_project_list'),
    path('new/', views.ProjectCreateView.as_view(), name='new_project'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='update_project'),
    #path('milestones/', views.MilestoneListView.as_view(), name='milestone_list'),
    path('milestones/', views.load_milestones, name='milestone_list'),
    path('ajax/load_task_milestoneI_list/', views.load_task_milestoneI_list, name='load_task_milestoneI_list'),
    path('milestones/new/', views.MilestoneCreateView.as_view(), name='new_milestone'),
    path('<int:pk>/', views.MilestoneUpdateView.as_view(), name='update_milestone'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/new/', views.TaskCreateView.as_view(), name='new_task'),
    path('<int:pk>/', views.TaskUpdateView.as_view(), name='update_task'),
    path('ajax/load-task-milestones/', views.load_task_milestones, name='load-task-milestones'),
]
