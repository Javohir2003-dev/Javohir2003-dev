from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from .serializers import UserSerializers,CategorySerialzers,Category_Fields_Serializers,Product_serializers,Product_Image_serializers
from .models import User, Category,Category_Field,Product,Product_Image
from rest_framework.views import APIView



class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'



class Register(ListCreateAPIView):
    queryset  = User.objects.all()
    serializer_class  = User



class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzers


class Category_Field_ListView(ListCreateAPIView):
    queryset = Category_Field.objects.all()
    serializer_class = Category_Fields_Serializers


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_serializers



class Product_image_ListView(ListCreateAPIView):
    queryset = Product_Image.objects.all()
    serializer_class = Product_Image_serializers




class SavatView(APIView):
    def get(self, request):
        id = request.user.id
        # print(dir(request.session))
        request.session.set_expiry(60) # during a minute
        # request.session.set_expiry(0) # until closing browser
        # request.session.set_expiry(None) # never die

        request.session[f'{id}'] = [1,2,3,5]
        if 'some' in request.session:
            print(request.session['some'])
        else:
            print('yoq')
        return Response({
            'message': 'Some message'
        })
    

    def post(self, request):
        request.session.set_expiry(60) # during a minute
        
        request.session['some'] = [1,2,3,5]
        print(request.session['some'])
        del request.session['some']
        return Response({
            'message': 'Some message'
        })

