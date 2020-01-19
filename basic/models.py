from django.db import models


class UserEntry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)
