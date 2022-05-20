from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Place
from .models import Place1

admin.site.register(Place)
admin.site.register(Place1)