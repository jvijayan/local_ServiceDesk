from django import forms

from django.db import models

from .models import Project, Milestone, Task, Document
from company_management.models import Company


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class OldProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'startdate', 'enddate', 'actual_startdate', 'actual_enddate', 'cost', 'project_manager', 'project_team', 'client', 'vendor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['client'].queryset = Company.objects.filter(typ=3)

        if 'client' in self.data:
            try:
                country_id = int(self.data.get('client'))
                # self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['client'].queryset = self.instance.client

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_status','name', 'startdate', 'enddate', 'actual_startdate', 'actual_enddate', 'cost', 'project_manager', 'project_team', 'client', 'vendor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Project'))

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ('name', 'project', 'startdate', 'enddate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'project', 'milestone', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Task'))
        self.fields['milestone'].queryset = Milestone.objects.none()

        #if 'project' in self.data:
        #    try:
        #        project_id = int(self.data.get('project'))
        #        self.fields['milestone'].queryset = Milestone.objects.filter(project_id=project_id).order_by('name')
        #    except (ValueError, TypeError):
        #        pass  # invalid input from the client; ignore and fallback to empty City queryset
        #elif self.instance.pk:
        #    self.fields['milestone'].queryset = self.instance.project.milestone_set.order_by('name')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )