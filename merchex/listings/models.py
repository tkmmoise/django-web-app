from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active = models.fields.BooleanField(default=True)
    official_page = models.fields.URLField(null=True, blank=True)
    # like_new = models.fields.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = 'RECORDS'
        CLOTHING = 'CLOTING'
        POSTERS = 'POSTERS'
        MISCELLANEOUS = 'MISCELLANEOUS'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=50)

    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    