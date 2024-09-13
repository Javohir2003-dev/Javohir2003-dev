from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from .serializers import UserSerializers,CategorySerialzers,Product_serializers,Product_Image_serializers
from .models import User, Category,Product,Product_Image
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions

 

class MyTokenView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).last()

        if user is not None:
            tokens = RefreshToken.for_user(user=user)
            message = {
                "refresh": str(tokens),
                "access": str(tokens.access_token),
                "username": user.username,
                "user_id": user.id,
                "status": user.status
            }
            return Response(message)
        return Response({
            'message': 'username yoki parol xato kiritildi'
        })
 

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





class ProductListView(APIView):
    def post(self, request):
        serializers = Product_serializers(data = request.data, context = {'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'yaratildi'})
        
        return Response({'message':'kiritilishda hatolik'})



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

