from django.contrib import admin
import app_landing.models

class BlockAdmin(admin.ModelAdmin):
    list_display = ('order', 'type', 'title')

class HighlightAdmin(admin.ModelAdmin):
    list_display = ('order', 'image')

admin.site.register(app_landing.models.Block, BlockAdmin)
admin.site.register(app_landing.models.Highlight, HighlightAdmin)

