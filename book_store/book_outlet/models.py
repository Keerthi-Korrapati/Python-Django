from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

#Data, Databases and Models
'''
    worked with data and SQL db => Built-in model feature
'''

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

# One-To-One Relation
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

#One-To-Many Relation
class Author(models.Model): #Base Author model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)# one-to-one relation with address model
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model): #class with extended built-in model
    # Fields or attributes of our data with value types 
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True, related_name="books") # calling Author model fields here  
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,null=False, db_index=True) #Harry Potter 1 => harry-potter-1 To create human-readable URLs.

    published_countries = models.ManyToManyField(Country, null = False)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    
    '''def save(self, *args, **kwargs):  # Overwriting Save => automatically generate slugs based on the title.
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)'''

    def __str__(self):
        return f"{self.title} ({self.rating})"