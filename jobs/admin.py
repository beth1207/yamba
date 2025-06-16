from django.contrib import admin
admin.site.site_header = "Yamba Administration"
admin.site.site_title = "Yamba Admin Portal"
admin.site.index_title = "Welcome to Yamba-Platform Job Management"

from .models import Job




@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'skills_required')


