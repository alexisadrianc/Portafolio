from django.contrib import admin


from .models import *


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'amenities', 'unit_qty')


class UnitAdmin(admin.ModelAdmin):
    model = Unit

    list_display = ('name', 'building_id', 'meter_qty', 'renter', 'init_date',  'expiration_date')


admin.site.register(Amenities)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(CommonExpenses)
admin.site.register(CommonExpensesLines)
admin.site.register(Garage)
admin.site.register(GarageLines)
