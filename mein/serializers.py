from .models import *
from rest_framework import serializers


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['user_id'] = user.id

        # ...

        return token









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
        fields = ['name','id']

    

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
    









#  Product Serializers


class Product_serializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'tur', 'name', 'price','batafsil']


    def create(self, validated_data):
        owner = self.context['request'].user
        new_product = Product.objects.create(**validated_data, user=owner)
        return new_product






#  Product_Image Serializers


class Product_Image_serializers(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = ['product', 'image']


    def create(self, validated_data):
        
        product_image = Product_Image.objects.create(**validated_data)
        return product_image


