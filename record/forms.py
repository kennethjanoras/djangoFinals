from django.forms import ModelForm
from django import forms
from .models import Department, Employee, Project, Task, TaskLog

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectForm(forms.ModelForm): 
    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class TaskLogForm(forms.ModelForm):
    class Meta:
        model = TaskLog
        fields = '__all__'
