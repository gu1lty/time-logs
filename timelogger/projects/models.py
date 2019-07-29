from django.db import models
from django.contrib.auth.models import User
class Projects:
    """Projects are general scope of work to be done"""

    name = models.CharField(max_length=50)
    description = models.TextField()
    user_id = models.ManyToManyField(User)

    def __str__(selft):
        return self.name
