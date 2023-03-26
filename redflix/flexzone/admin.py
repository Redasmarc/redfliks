from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    list_display_links = ('title',)
    list_filter = ('release_date',)
    search_fields = ('title',)
    #list_editable = ('release_date',)

class MovieInline(admin.TabularInline):
    model = models.Movie
    extra = 0

admin.site.register(models.User)
admin.site.register(models.Genre)
admin.site.register(models.Producer)
admin.site.register(models.Actor)
admin.site.register(models.TvShow)
admin.site.register(models.Movie, MovieAdmin)