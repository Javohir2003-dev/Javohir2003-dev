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
    rasm = models.ImageField(upload_to='category_rasm/')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='tur')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    


class Category_Field(models.Model):
    rasm = models.ImageField(upload_to='category_field_rasm/')
    name = models.CharField(max_length=100,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')


    def __str__(self):
        return self.name



class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tur = models.ForeignKey(Category_Field, on_delete=models.CASCADE, related_name='tur')
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    price = models.TextField()
    batafsil = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    

class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_image/')