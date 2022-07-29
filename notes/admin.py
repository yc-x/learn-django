from django.contrib import admin
from . import models
# Register your models here.

# get it appears in the default admin interface.
class NotesAdmin(admin.ModelAdmin):
    # pass
    # modify how it appears in admin panel
    list_display = ('title',)   # this is a tuple

admin.site.register(models.Notes, NotesAdmin)