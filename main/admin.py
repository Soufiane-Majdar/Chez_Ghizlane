from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'date', 'time', 'phone', 'created_at', 'email')
    list_filter = ('service', 'date', 'created_at')
    search_fields = ('name', 'email', 'phone')
    ordering = ('-date', '-time')
    date_hierarchy = 'date'
    
    fieldsets = (
        (_('Informations Client'), {
            'fields': ('name', 'email', 'phone')
        }),
        (_('Détails Réservation'), {
            'fields': ('service', 'date', 'time')
        }),
        (_('Notes'), {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
    
    list_per_page = 20
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('created_at',)
        return ()
