from django.db import models
from projects.models import Projects

class ProjectTasks:
    """Tasks For Each Project"""

    name = models.CharField(max_length=50)
    decription = models.TextField()

    # 0 = On Hold
    # 1 = New Task
    # 2 = Ongoing
    # 3 = Completed
    status = models.IntegerField(default=1)

    #Man Days
    task_estimate = models.FloatField(default=1.00)

    def __str__(self):
        return self.name
