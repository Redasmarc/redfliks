from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class User(models.Model):
    id = models.UUIDField(_('ID'), primary_key=True, default=uuid.uuid4)
    email = models.CharField(_('email address'), max_length=128, db_index=True)
    password = models.CharField(_('password'), max_length=128, db_index=True)
    first_name = models.CharField(_('first name'), max_length=128, blank=True)
    last_name = models.CharField(_('last name'), max_length=128, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=128, blank=True)

    def __str__(self) -> str:
        return f"{self.email} , {self.id}"
    
    class Meta:
        ordering = ['email', 'password', 'first_name', 'last_name', 'phone_number']


class Genre(models.Model):
    genre_name = models.CharField(_('genre'), max_length=50, db_index=True)

    def __str__(self) -> str:
        return f"{self.genre_name}"
    
    class Meta:
        ordering = ['genre_name']


class Producer(models.Model):
    producer_f_name = models.CharField(_('first name'), max_length=50, db_index=True)
    producer_l_name = models.CharField(_('last name'), max_length=50, db_index=True)

    def __str__(self) -> str:
        return f"{self.producer_f_name} {self.producer_l_name}"
    
    class Meta:
        ordering = ['producer_f_name', 'producer_l_name']


class Actor(models.Model):
    actor_f_name = models.CharField(_('first name'), max_length=50, db_index=True)
    actor_l_name = models.CharField(_('last name'), max_length=50, db_index=True)

    def __str__(self) -> str:
        return f"{self.actor_f_name} {self.actor_l_name}"
    
    class Meta:
        ordering = ['actor_f_name', 'actor_l_name']

class Movie(models.Model):
    image = models.ImageField(_('thumbnail'), upload_to='flexzone/thumbnails/', null=True, blank=True)
    title = models.CharField(_('movie name'), max_length=100, db_index=True)
    description = models.TextField(_('description'))
    trailer = models.URLField(null=True, blank=True)
    SUB_GROUP = (
        ('-', _('---------')),
        ('n', _('Nitflex')),
        ('h', _('HPO')),
        ('d', _('Disnep+')),
    )
    status = models.CharField(_('group'), max_length=1, choices=SUB_GROUP, default='-')
    genres = models.ManyToManyField(
        Genre,
        verbose_name=_('Genres'),
    )
    producers = models.ManyToManyField(
        Producer,
        verbose_name=(_('producer'))
    )
    release_date = models.DateField(_("publish date"), auto_now=False, auto_now_add=False)
    actors = models.ManyToManyField(
        Actor,
        verbose_name=(_('actors')),
)
    
    def __str__(self) -> str:
        return f"{self.title} {self.release_date}"
    
    class Meta:
        ordering = ['title', 'description', 'genres__genre_name', 'producers__producer_f_name', 'producers__producer_l_name', 'release_date', 'actors__actor_f_name', 'actors__actor_l_name']



class TvShow(models.Model):
    show_name = models.CharField(_('show name'), max_length=100, db_index=True)
    description = models.TextField(_('description'))
    season = models.IntegerField(_('season'))
    episode = models.IntegerField(_('episode'))
    genres = models.ManyToManyField(
        Genre,
        verbose_name=_('Genres'),
    )
    producers = models.ManyToManyField(
        Producer,
        verbose_name=(_('producer')),
    )
    release_date = models.DateField(_("publish date"), auto_now=False, auto_now_add=False)
    actors = models.ManyToManyField(
        Actor,
        verbose_name=(_('actors')),
)
    
    def __str__(self) -> str:
        return f"{self.show_name} S{self.season}E{self.episode} "
    
    class Meta:
        ordering = ['show_name', 'description', 'season', 'episode', 'genres__genre_name', 'producers__producer_f_name', 'producers__producer_l_name', 'release_date', 'actors__actor_f_name', 'actors__actor_l_name']
