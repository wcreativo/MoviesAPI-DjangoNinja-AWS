from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title}"
