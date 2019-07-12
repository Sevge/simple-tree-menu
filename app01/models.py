from django.db import models
from mptt.models import MPTTModel

# Create your models here.


class MPTTtree(MPTTModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=True, related_name='children')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
