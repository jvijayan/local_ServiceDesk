from django.views import generic
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from .forms import UserForm, UserTeamMeamberForm

from .models import User, UserGroup, UserTeam, UserTeamMember

# Used to add new users
class AddUser(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'gender', 'company'
              , 'branch', 'department', 'usergroup', 'category'
              , 'username', 'password']
    template_name = 'user_management/addUser.html'
    success_url = reverse_lazy('listUsers')

# All user groups list view
class ListUsers(ListView):
    template_name = 'user_management/listUsers.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all()

# Detailed view of a specific user
class DetailsUser(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'user_management/detailsUser.html'
    
class UpdateUser(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'gender', 'company'
              , 'branch', 'department', 'usergroup', 'category'
              , 'username', 'password']
    template_name = 'user_management/updateUser.html'
    success_url = reverse_lazy('listUsers')

# Used to add new user groups
class AddUserGroup(CreateView):
    model = UserGroup
    fields = ['name',]
    template_name = 'user_management/addUserGroup.html'
    success_url = reverse_lazy('listUserGroups')

# All user groups list view
class ListUserGroups(ListView):
    template_name = 'user_management/listUserGroups.html'
    context_object_name = 'all_userGroups'

    def get_queryset(self):
        return UserGroup.objects.all()

# Detailed view of a specific user group
class DetailsUserGroup(DetailView):
    model = UserGroup
    context_object_name = 'userGroup'
    template_name = 'user_management/detailsUserGroup.html'
    
class UpdateUserGroup(UpdateView):
    model = UserGroup
    fields = ['name', ]
    template_name = 'user_management/updateUserGroup.html'
    success_url = reverse_lazy('listUserGroups')

# Used to add new teams
class AddTeam(CreateView):
    model = UserTeam
    fields = ['name', ]
    template_name = 'user_management/addTeam.html'
    success_url = reverse_lazy('listTeams')

# All user groups list view
class ListTeams(ListView):
    template_name = 'user_management/listTeams.html'
    context_object_name = 'all_teams'

    def get_queryset(self):
        return UserTeam.objects.all()

# Detailed view of a specific user group
class DetailsTeam(DetailView):
    model = UserTeam
    context_object_name = 'team'
    template_name = 'user_management/detailsTeam.html'
    
class UpdateTeam(UpdateView):
    model = UserTeam
    fields = ['name', ]
    template_name = 'user_management/updateTeam.html'
    success_url = reverse_lazy('listTeams')




# Used to add new user groups
class AddUserToTeam(CreateView):
    model = UserTeamMember
    fields = ['user','user_team']
    template_name = 'user_management/addUserToTeam.html'
    success_url = reverse_lazy('listTeams')

def load_teams(request):
    #project_id = request.GET.get('project')
    #milestones = Milestone.objects.filter(project_id=project_id).order_by('name')
    userGroups = UserTeam.objects.all
    return render(request, 'user_management/listUserGroupsExtended.html', {'userGroups': userGroups})

def load_team_members(request):
    project_id = request.GET.get('project')
    members = UserTeamMember.objects.filter(user_team=project_id) #.order_by('name')
    #members = UserTeamMember.objects.all
    return render(request, 'user_management/team_member_dropdown_list_options.html', {'members': members})
