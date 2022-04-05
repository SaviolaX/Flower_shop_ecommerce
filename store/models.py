from distutils.command.upload import upload
from itertools import product
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200, db_index=True)
    category_image = models.ImageField(upload_to='category_images/')
    category_slug = models.SlugField(max_length = 250, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self) -> str:
        return self.category_name
    

class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=200, db_index=True)
    product_slug = models.SlugField(max_length=200, db_index=True)
    product_image = models.ImageField(upload_to='product_images/')
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        index_together = (('id', 'product_slug'),)
    
    def __str__(self) -> str:
        return self.product_name

