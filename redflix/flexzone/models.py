from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class SubscriptionPack(models.Model):
    id = models.UUIDField(_('ID'), primary_key=True, default=uuid.uuid4)
    pack = models.CharField(_('subscription pack'), max_length=100)

    def __str__(self) -> str:
        return f"{self.pack}"
    
    class Meta:
        ordering = ['pack']
    
    def display_movies(self):
        return ', '.join(movie.movie_name for movie in self.movies.all())
    display_movies.short_description=_('movies')


class User(models.Model):
    id = models.UUIDField(_('ID'), primary_key=True, default=uuid.uuid4)
    email = models.CharField(_('email address'), max_length=128, db_index=True)
    password = models.CharField(_('password'), max_length=128, db_index=True)
    first_name = models.CharField(_('first name'), max_length=128, blank=True)
    last_name = models.CharField(_('last name'), max_length=128, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=128, blank=True)
    subscription = models.ManyToManyField(
        SubscriptionPack,
        verbose_name=_("subscription"), 
        # on_delete=models.CASCADE,
        # null=True
        )

    def __str__(self) -> str:
        return f"{self.email} , {self.id} , {self.subscription}"
    
    class Meta:
        ordering = ['email', 'password', 'first_name', 'last_name', 'phone_number', 'subscription__pack']


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
    movie_name = models.CharField(_('movie name'), max_length=100, db_index=True)
    description = models.TextField(_('description'))
    subscription_pack = models.ForeignKey(
        SubscriptionPack,
        related_name='movies',
        verbose_name=_("subscription package"), 
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
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
        return f"{self.movie_name} {self.release_date}"
    
    class Meta:
        ordering = ['movie_name', 'description', 'subscription_pack', 'genres__genre_name', 'producers__producer_f_name', 'producers__producer_l_name', 'release_date', 'actors__actor_f_name', 'actors__actor_l_name']



class TvShow(models.Model):
    show_name = models.CharField(_('show name'), max_length=100, db_index=True)
    description = models.TextField(_('description'))
    subscription_pack = models.ForeignKey(
        SubscriptionPack,
        verbose_name=_("subscription package"), 
        on_delete=models.CASCADE,
        null=True,
    )
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
        ordering = ['show_name', 'description', 'subscription_pack', 'season', 'episode', 'genres__genre_name', 'producers__producer_f_name', 'producers__producer_l_name', 'release_date', 'actors__actor_f_name', 'actors__actor_l_name']
