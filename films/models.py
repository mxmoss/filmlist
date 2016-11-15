from django.db import models

class Genre(models.Model):
    description = models.CharField(max_length=20, blank=True, default='')
    class Meta:
        ordering = ('description',)

class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year_prod = models.IntegerField(blank=True,)
    genre = models.ForeignKey(Genre,blank=True,)
    theaters = models.ManyToManyField('Theater', blank=True,)
    class Meta:
#        ordering = ('title',)
        ordering = ('id',)

class Theater(models.Model):
    name = models.CharField(max_length=40, blank=True, default='')
    city = models.CharField(max_length=40, blank=True, default='')
    state = models.CharField(max_length=2, blank=True, default='')
    num_screens = models.IntegerField()
    digital = models.BooleanField()
    comment_txt = models.CharField(max_length=255, blank=True, default='')
#    films = models.ManyToManyField('Film', blank=True,)
    class Meta:
#        ordering = ('state', 'city', 'name',)
        ordering = ('id',)

