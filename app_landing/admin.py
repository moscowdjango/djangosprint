from django.contrib import admin
import app_landing.models

class BlockAdmin(admin.ModelAdmin):
    list_display = ('order', 'type', 'title')

class HighlightAdmin(admin.ModelAdmin):
    list_display = ('order', 'image', 'description')

class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'description')

class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('order', 'image', 'description')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('order', 'image', 'description')

admin.site.register(app_landing.models.Block, BlockAdmin)
admin.site.register(app_landing.models.Highlight, HighlightAdmin)
admin.site.register(app_landing.models.ScheduleItem, ScheduleItemAdmin)
admin.site.register(app_landing.models.Organizer, OrganizerAdmin)
admin.site.register(app_landing.models.Sponsor, SponsorAdmin)

