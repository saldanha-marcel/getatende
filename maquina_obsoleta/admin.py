import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import SerialNumber


@admin.register(SerialNumber)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('id_serial','number_serial',)
    search_fields = ('number_serial',)
    ordering = ('id_serial',)
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response ['Content-Disposition' ] = 'attachment; filename="Seriais.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'serial'])
        for serial in queryset:
            writer.writerow([serial.id_serial, serial.number_serial])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]