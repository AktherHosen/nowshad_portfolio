from django.contrib import admin
from . models import PortfolioProject,Category
# Register your models here.

admin.site.register(Category)
admin.site.register(PortfolioProject)