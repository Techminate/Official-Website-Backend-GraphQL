from django.db import models
from .jobs import Jobs

class Tasks(models.Model):
    job = models.ForeignKey(Jobs, related_name='tasks', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    bounty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.job.title} | {self.title}"

    class Meta:
        verbose_name_plural='Tasks'