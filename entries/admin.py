# entries/admin.py
from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    # Columnas que se muestran en la lista
    list_display = ['title', 'created_at', 'mood', 'temperature']
    
    # Filtros en el sidebar
    list_filter = ['created_at', 'mood']
    
    # Campos de búsqueda
    search_fields = ['title', 'content']
    
    # Ordenamiento por defecto
    ordering = ['-created_at']
    
    # Campos de solo lectura
    readonly_fields = ['created_at', 'updated_at']
    
    # Organizar campos en el formulario
    fieldsets = (
        ('Información básica', {
            'fields': ('title', 'content')
        }),
        ('Estado de ánimo y clima', {
            'fields': ('mood', 'weather_icon', 'temperature', 'location')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Sección colapsable
        }),
    )
    
    # Paginación
    list_per_page = 20

# Registrar con la configuración personalizada
admin.site.register(Entry, EntryAdmin)