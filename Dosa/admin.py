from django.contrib import admin
from . import models


admin.site.site_header="Admin"
admin.site.register(models.ParentCategory)
admin.site.register(models.SubCategory)
admin.site.register(models.Product)
admin.site.register(models.ProductVoting)
admin.site.register(models.Slider)
