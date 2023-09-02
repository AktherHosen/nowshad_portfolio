from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/profile', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name