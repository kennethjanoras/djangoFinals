from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Department, Employee, Project, Task, TaskLog
from .forms import DepartmentForm, EmployeeForm, ProjectForm, TaskForm, TaskLogForm

class HomePageView(ListView):
    model = Employee
    context_object_name = 'home'
    template_name = "base.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context

class DepartmentListView(ListView):
    model = Department
    template_name = 'dept_list.html'
    context_object_name = 'departments'
    paginate_by = 5

    def get_queryset(self):
        return Department.objects.all()

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'dept_add.html'
    success_url = reverse_lazy('department-list')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'dept_edit.html'
    success_url = reverse_lazy('department-list')

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'dept_del.html'
    success_url = reverse_lazy('department-list')
    
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    paginate_by = 5

    def get_queryset(self):
        return Employee.objects.all()

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_add.html'
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_edit.html'
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_del.html'
    success_url = reverse_lazy('employee-list')

class ProjectListView(ListView):
    model = Project
    template_name = 'proj_list.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.all()

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'proj_add.html'
    success_url = reverse_lazy('project-list')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'proj_edit.html'
    success_url = reverse_lazy('project-list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'proj_del.html'
    success_url = reverse_lazy('project-list')

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.all()

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_add.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

class TaskLogListView(ListView):
    model = TaskLog
    template_name = 'tsklog_list.html'
    context_object_name = 'tasklogs'
    paginate_by = 5

    def get_queryset(self):
        return TaskLog.objects.all()

class TaskLogCreateView(CreateView):
    model = TaskLog
    form_class = TaskLogForm
    template_name = 'tsklog_add.html'
    success_url = reverse_lazy('tsklog-list')

class TaskLogUpdateView(UpdateView):
    model = TaskLog
    form_class = TaskLogForm
    template_name = 'tsklog_edit.html'
    success_url = reverse_lazy('tsklog-list')

class TaskLogDeleteView(DeleteView):
    model = TaskLog
    template_name = 'tsklog_del.html'
    success_url = reverse_lazy('tsklog-list')


# Similar classes for Employee, Project, Task, and TaskLog...
