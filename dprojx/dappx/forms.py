from django import forms
from django.contrib.auth.models import User
from dappx.models import ProjectInfo
class ProjectForm(forms.ModelForm):
    class Meta():
        model = ProjectInfo
        fields = ('project_name', 'project_creators', 'project_direction', 'project_root','project_picture', 'project_text_task', 'project_text_methods', 'project_text_results', 'project_text_discussions', 'project_text_conclusions', 'project_wins')
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
class SortForm(forms.Form):
    direction = forms.CharField()
