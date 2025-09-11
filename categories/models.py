from django.db import models




class Categories(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Create your models here.
