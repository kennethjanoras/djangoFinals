from django.contrib import admin
from django.urls import path
from record import views  # Replace 'your_app_name' with your actual app name
from record.views import (
    DepartmentListView,
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDeleteView,
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskLogListView,  
    TaskLogCreateView,
    TaskLogUpdateView,
    TaskLogDeleteView,
)

# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/add/', DepartmentCreateView.as_view(), name='department-add'),
    path('departments/<int:pk>/', DepartmentUpdateView.as_view(), name='department-update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employees/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/add/', ProjectCreateView.as_view(), name='project-add'),
    path('projects/<int:pk>/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasklogs/', TaskLogListView.as_view(), name='tasklog-list'),
    path('tasklogs/add/', TaskLogCreateView.as_view(), name='tasklog-add'),
    path('tasklogs/<int:pk>/', TaskLogUpdateView.as_view(), name='tasklog-update'),
    path('tasklogs/<int:pk>/delete/', TaskLogDeleteView.as_view(), name='tasklog-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

