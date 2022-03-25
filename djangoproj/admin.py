from django.contrib import admin
from django.core.management import call_command
from djangoproj import models


@admin.action(description='Parse excel files')
def parse_excel(modeladmin, request, queryset):
    for excel_object in queryset:
        call_command('loadfabricdata', excel_object.file.path)


class ExcelAdmin(admin.ModelAdmin):
    actions = [parse_excel]


admin.site.register(models.TransportDelivery)
admin.site.register(models.SteelStructureFabric)
admin.site.register(models.DeliveryObject)
admin.site.register(models.ExcelFile, ExcelAdmin)
