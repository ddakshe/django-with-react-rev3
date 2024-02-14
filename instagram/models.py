from django.db import models

from askcompany import settings
from askcompany.models import BaseModel


class Post(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.message
