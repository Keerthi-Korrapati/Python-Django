from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

#Data, Databases and Models
'''
    worked with data and SQL db => Built-in model feature
'''


class Book(models.Model): #class with extended built-in model
    # Fields or attributes of our data with value types 
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) #Harry Potter 1 => harry-potter-1

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):  # Overwriting Save
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"