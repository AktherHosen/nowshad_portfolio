from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    def __str__(self):
        return self.cat_name
    
class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    screenshoot = models.ImageField(upload_to='images/projects/')
    technologies = models.CharField(max_length=100)
    project_url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
    ]
class ProjectReview(models.Model):
    reviews = models.CharField(max_length=200)
    ratings = models.IntegerField(choices=RATING_CHOICES)
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)
    def __str__(self):
        return self.reviews