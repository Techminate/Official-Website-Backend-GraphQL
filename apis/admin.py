from django.contrib import admin

# Register your models here.
from .models.jobs import Jobs
from .models.tasks import Tasks

admin.site.register(Jobs)
admin.site.register(Tasks)