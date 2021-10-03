from django.contrib import admin

# Register your models here.
from .models.jobs import Jobs

admin.site.register(Jobs)
