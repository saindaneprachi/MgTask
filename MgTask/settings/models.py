from django.db import models
from authentication.models import BaseClass

# Create your models here.
class Workspace(BaseClass):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_json(self):
        return dict(
            id=self.id,
            title=self.title,
            created=self.created,
            modified=self.modified,
        )






