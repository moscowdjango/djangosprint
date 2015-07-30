from django.contrib import admin
import app_landing.models

class BlockAdmin(admin.ModelAdmin):
    list_display = ('order', 'type', 'title')

class HighlightAdmin(admin.ModelAdmin):
    list_display = ('order', 'image')

class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'description')

admin.site.register(app_landing.models.Block, BlockAdmin)
admin.site.register(app_landing.models.Highlight, HighlightAdmin)
admin.site.register(app_landing.models.ScheduleItem, ScheduleItemAdmin)

