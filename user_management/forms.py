from .models import User, UserGroup, UserTeamMember
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'company'
              , 'branch', 'department', 'usergroup', 'category'
              , 'username', 'password')
        
class UserGroupForm(forms.ModelForm):

    class Meta:
        model = UserGroup
        fields = ('name',)

class UserTeamMeamberForm(forms.ModelForm):

    class Meta:
        model = UserTeamMember
        fields = ('user','user_team')

# class UserForm(forms.ModelForm):
# 
#     class Meta:
#         model = User
#         exclude = ['user_id']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control input-flat'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control input-flat'}),
#             'username': forms.TextInput(attrs={'class': 'form-control input-flat'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control input-flat'}),
#             'gender': forms.Select(attrs={'class': 'form-control input-flat'}),
#             'company': forms.Select(attrs={'class': 'form-control input-flat'}),
#             'branch': forms.Select(attrs={'class': 'form-control input-flat'}),
#             'department': forms.Select(attrs={'class': 'form-control input-flat'}),
#             'usergroup': forms.Select(attrs={'class': 'form-control input-flat'})
#         }
