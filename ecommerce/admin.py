import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import CnpjEcommerce

@admin.register(CnpjEcommerce)
class CnpjAdmin(admin.ModelAdmin):
    list_display = ('id_cnpj','number_cnpj',)
    search_fields = ('number_cnpj',)
    ordering = ('id_cnpj',)
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response ['Content-Disposition' ] = 'attachment; filename="CNPJs.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'CNPJ'])
        for cnpj in queryset:
            writer.writerow([cnpj.id_cnpj, cnpj.number_cnpj])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]