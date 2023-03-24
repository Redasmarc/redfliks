from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models

class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'release_date', 'subscription_pack')
    list_display_links = ('movie_name',)
    list_filter = ('release_date', 'subscription_pack')
    search_fields = ('movie_name',)
    #list_editable = ('release_date',)

class MovieInline(admin.TabularInline):
    model = models.Movie
    extra = 0
    

class SubscriptionPackAdmin(admin.ModelAdmin):
    list_display = ('pack', 'display_movies')
    list_display_links = ('pack',)
    inlines = [
        MovieInline,
    ]

admin.site.register(models.User)
admin.site.register(models.Genre)
admin.site.register(models.Producer)
admin.site.register(models.Actor)
admin.site.register(models.TvShow)
admin.site.register(models.SubscriptionPack, SubscriptionPackAdmin)
admin.site.register(models.Movie, MovieAdmin)