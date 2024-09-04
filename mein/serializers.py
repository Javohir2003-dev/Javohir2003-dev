from .models import *
from rest_framework import serializers

# UserSerializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'image', 'status']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password('password')
        user.save()
        return user 
    



# Category_Serializers

class CategorySerialzers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','rasm']

    

    def create(self, validated_data):
        if Category.objects.filter(name = validated_data['name']).exists():
            raise serializers.ValidationError('bu category mavjud !')
        
        category = Category.objects.create(**validated_data)
        return category
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rasm = validated_data.get('rasm', instance.rasm)
        instance.save()
        return instance
    




# Category_Fields_Serializers

class Category_Fields_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Category_Field
        fields = ['rasm', 'name', 'category']
    
    def create(self, validated_data):

        if Category_Field.objects.filter(name = validated_data['name']).exists():
            raise serializers.ValidationError('bu category allaqachon mavjud !')
        
        category_field = Category_Field.objects.create(**validated_data)
        return category_field
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rasm = validated_data.get('rasm', instance.rasm)
        instance.save()
        return instance




#  Product Serializers


class Product_serializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['user', 'tur', 'name', 'price']


    def create(self, validated_data):
        
        product = Product.objects.create(**validated_data)
        return product







#  Product_Image Serializers


class Product_Image_serializers(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = ['product', 'image']


    def create(self, validated_data):
        
        product_image = Product_Image.objects.create(**validated_data)
        return product_image


