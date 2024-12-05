from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import (
    Booking, Service, Gallery, Testimonial,
    TeamMember, SiteSettings, Promotion
)

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

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'display_image', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    ordering = ('order',)
    list_editable = ('order', 'is_active')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "No image"
    display_image.short_description = _('Image')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'display_image', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title',)
    ordering = ('order',)
    list_editable = ('order', 'is_active')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "No image"
    display_image.short_description = _('Image')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_photo', 'rating', 'order', 'is_active')
    list_filter = ('rating', 'is_active')
    search_fields = ('name', 'comment')
    ordering = ('order',)
    list_editable = ('order', 'is_active')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 25px;" />', obj.photo.url)
        return "No photo"
    display_photo.short_description = _('Photo')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'display_photo', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'position', 'description')
    ordering = ('order',)
    list_editable = ('order', 'is_active')

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 25px;" />', obj.photo.url)
        return "No photo"
    display_photo.short_description = _('Photo')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Général'), {
            'fields': ('site_name', 'logo', 'favicon')
        }),
        (_('Section Hero'), {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image')
        }),
        (_('Informations de Contact'), {
            'fields': ('phone', 'email', 'address', 'google_maps_link')
        }),
        (_('Réseaux Sociaux'), {
            'fields': ('facebook', 'instagram', 'tiktok')
        }),
        (_('Horaires'), {
            'fields': ('business_hours',)
        }),
        (_('Pied de Page'), {
            'fields': ('footer_text',)
        }),
        (_('Section À Propos'), {
            'fields': ('about_title', 'about_content', 'about_image')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'start_date', 'end_date', 'is_active', 'order')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    ordering = ('-start_date', 'order')
    list_editable = ('is_active', 'order')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "No image"
    display_image.short_description = _('Image')
