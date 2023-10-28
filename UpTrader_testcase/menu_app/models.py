from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
