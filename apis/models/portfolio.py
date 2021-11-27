from django.db import models

class Portfolio(models.Model):
    DESIGN = 'design'
    WEBSITE = 'website'
    APP = 'app'

    CHOICES_CATEGORY = (
        (DESIGN, 'Design'),
        (WEBSITE, 'Wesite'),
        (APP, 'App')
    )

    category = models.CharField(max_length=20, choices=CHOICES_CATEGORY, default=WEBSITE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/portfolio/")
    link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.category} | {self.title}"

    class Meta:
        verbose_name_plural='Portfolio'