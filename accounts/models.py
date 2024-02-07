from django.contrib.auth.models import AbstractUser

from askcompany.models import BaseModel


class User(BaseModel, AbstractUser):
    pass