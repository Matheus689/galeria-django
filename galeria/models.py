from django.db import models

# Create your models here.
class Pais(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tourism = models.TextField()
    image = models.ImageField(upload_to='galeria/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['title']