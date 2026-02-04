from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'completed_date', 'order', 'image_preview')
    list_filter = ('featured', 'completed_date', 'technologies')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('featured', 'order')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Osnovne informacije', {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Tehnologije', {
            'fields': ('technologies',)
        }),
        ('Slike', {
            'fields': ('image', 'screenshot_1', 'screenshot_2')
        }),
        ('Linkovi', {
            'fields': ('github_url', 'live_url')
        }),
        ('Status i redosled', {
            'fields': ('featured', 'completed_date', 'order')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover;" />')
        return "Nema slike"
    
    image_preview.short_description = "Slika"