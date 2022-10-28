from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField('Категория', max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField('Услуга', max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Salon(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name

class ProstoModel(models.Model):
    title = models.CharField(max_length=255)
    qqqqq = models.CharField(max_length=255)
    wwwww = models.CharField(max_length=255)

# Create your models here.
