from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Classification)
admin.site.register(ActivityType)
admin.site.register(Supplier)
admin.site.register(Services)
admin.site.register(State)
admin.site.register(City)
