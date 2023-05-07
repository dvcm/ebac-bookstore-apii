from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
