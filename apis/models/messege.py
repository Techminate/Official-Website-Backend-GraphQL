from django.db import models

class Messege(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    messege = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} | {self.address}"

    class Meta:
        verbose_name_plural='Messege'