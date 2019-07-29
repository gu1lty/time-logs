from django.db import models
from projectTasks.models import ProjectTasks
from userDetails.models import UserDetails
from datetime import datetime

class TimeLogs:
    """Logging effort done for each task"""
    task = models.ForeignKey(ProjectTasks, id)
    user = models.ForeignKey(UserDetails, id)
    timeStart = models.DateTimeField()
    timeEnd = models.DateTimeField()
    workDone = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
