from django.contrib import admin
from .models import Department, Employee, Project, Task, TaskLog

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'created_at', 'updated_at')
    search_fields = ("FirstName", "LastName", "Email", "Department")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'department', 'created_at', 'updated_at')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'deadline', 'project', 'created_at', 'updated_at')

    filter_horizontal = ('assignees',)  # To display assignees in a horizontal widget

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('assignees')

@admin.register(TaskLog)
class TaskLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'log_date', 'log_details', 'created_at', 'updated_at')

    # Assuming log_date, log_details are fields in the TaskLog model
    def log_date(self, obj):
        return obj.log_date  # Replace with the correct attribute name from the TaskLog model
    
    def log_details(self, obj):
        return obj.log_details  # Replace with the correct attribute name from the TaskLog model
