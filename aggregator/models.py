from django.db import models


class Episode(models.Model):
    podcast_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    guid = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"
