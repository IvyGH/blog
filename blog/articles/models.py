from django.db import models
from django.urls import reverse

class Article(models.Model):
    """ Article model class """
    title = models.CharField(max_length=320)
    text = models.TextField()
    author = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
