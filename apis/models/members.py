from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Team'

class Member(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    gmail = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    discord = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/members/")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.name} | Role: {self.role} | Team: {self.Team.name}"

    class Meta:
        verbose_name_plural = "Members"
