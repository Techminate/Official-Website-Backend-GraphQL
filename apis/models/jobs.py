from django.db import models

class Jobs(models.Model):
    projectName = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    requirements = models.CharField(max_length=100)
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.projectName} | {self.title}"

    class Meta:
        verbose_name_plural='Jobs'