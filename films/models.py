from django.db import models

class Genre(models.Model):
    description = models.CharField(max_length=20, blank=True, default='')
    owner = models.ForeignKey(
        'auth.User',
        related_name='genres',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ('description',)

    def __str__(self):
        return self.description


class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year_prod = models.IntegerField(blank=True, )
    genre = models.ForeignKey(Genre, )
    owner = models.ForeignKey(
        'auth.User',
        related_name='films', #instead of film_set you can just use films
        on_delete=models.CASCADE,
        null=True,
    )

    #    theaters = models.ManyToManyField('Theater', blank=True,)
    class Meta:
        #        ordering = ('title',)
        ordering = ('-title',)

    def __str__(self):
        return self.title

class Theater(models.Model):
    name = models.CharField(max_length=40, blank=True, default='')
    city = models.CharField(max_length=40, blank=True, default='')
    state = models.CharField(max_length=2, blank=True, default='')
    num_screens = models.IntegerField(blank=True,)
    digital = models.BooleanField()
    comment_txt = models.CharField(max_length=255, blank=True, default='')
    films = models.ManyToManyField(Film)
    owner = models.ForeignKey(
        'auth.User',
        related_name='theaters', #instead of filme_set you can just use films
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        #        ordering = ('state', 'city', 'name',)
        ordering = ('id',)

    def __str__(self):
        return self.name
