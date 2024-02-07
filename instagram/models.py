from django.db import models

from askcompany.models import BaseModel


class Post(BaseModel):
    message = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.message
