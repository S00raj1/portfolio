from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.name

class BlogData(models.Model):
    title =  models.CharField(max_length=120, null=False, blank=False)
    Content = models.TextField(null=False, blank=False)
    publication_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to="blog-image", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('publication_date',) 
