from django.apps import AppConfig

class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'record'  # Replace 'your_app_name' with your actual app name

    #def ready(self):
       # pass  # You can put initialization code here if needed
