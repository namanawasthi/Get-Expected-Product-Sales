from django.db import models

# Create your models here.
class ParentCategory(models.Model):
    parent_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='parent_category/')

    def __str__(self):
        return self.parent_name

class SubCategory(models.Model):
    parent = models.ForeignKey(ParentCategory,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sub_category/')

    def __str__(self):
        return self.sub_name

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product/')
    price = models.CharField(max_length=50)
    Type = models.TextField()
    size_or_weight = models.CharField(max_length=100)
    MOQ = models.TextField()
    box_dimension = models.CharField(max_length=100)
    Packaging = models.CharField(max_length=100)
    Availability = models.CharField(max_length=100)
    youtube_link = models.TextField()
    background_image = models.ImageField(upload_to='background/',default="None")

    
    def __str__(self):
        return self.name+" - "+self.sub_category.parent.parent_name


class ProductVoting(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    total_vote = models.IntegerField(default=0)
    yes = models.IntegerField(default=0)
    no = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name


class Slider(models.Model):
    images = models.ImageField(upload_to="slider/")

    
