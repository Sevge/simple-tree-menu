from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from app01.models import MPTTtree

# Register your models here.

admin.site.register(MPTTtree, MPTTModelAdmin)