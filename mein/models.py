from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):

    STATUS = (
        ('admin', 'Admin'),
        ('user', 'User')
    )

    status = models.CharField(max_length=50, choices=STATUS, default='user')
    image = models.ImageField(upload_to='user/', default='user.png')



class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    rasm = models.ImageField(upload_to='category_rasm/', null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='category')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    



class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tur = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='turlar')
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    price = models.TextField()
    batafsil = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    

class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_image/')