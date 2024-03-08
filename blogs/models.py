from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    blog_image = models.ImageField(upload_to='images/blogs')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    url = models.URLField( blank = True, null = True)
    def __str__(self):
        return self.title