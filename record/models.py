from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True        
    def __str__(self):
        return f"{self.__class__.__name__} - {self.id}"

class Department(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    ProfileImage = models.ImageField(upload_to='employee_images/',blank=True, null=True)

    def __str__(self):
        return self.name

class Project(BaseModel):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name

class Task(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignees = models.ManyToManyField(Employee, related_name='tasks_assigned')

    def __str__(self):
        return self.title
    
class TaskLog(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_logs')
    action = models.CharField(max_length=100)
    performed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='performed_tasks')

    def __str__(self):
        return f"{self.task} - {self.action}"

