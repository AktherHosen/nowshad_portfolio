from django.contrib import admin
from . models import PortfolioProject,Category,ProjectReview
# Register your models here.

admin.site.register(Category)
admin.site.register(PortfolioProject)
admin.site.register(ProjectReview)