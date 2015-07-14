from django.contrib import admin
import app_landing.models

class BlockAdmin(admin.ModelAdmin):
    list_display = ('type', 'title')

admin.site.register(app_landing.models.Block, BlockAdmin)

