from django.contrib import admin

# Register your models here.
from . models import picture
admin.site.register(picture)

from . models import my_team
admin.site.register(my_team)