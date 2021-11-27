from django.contrib import admin

# Register your models here.
from .models.jobs import Jobs
from .models.tasks import Tasks
from .models.members import Team, Member
from .models.portfolio import Portfolio

admin.site.register(Jobs)
admin.site.register(Tasks)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Portfolio)