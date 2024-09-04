
from django.urls import path,include
from . import views as a



urlpatterns = [
   path('create/', a.UserCreateListView.as_view(), name='user_create'),
   path('detail/<int:id>/', a.UserDetailView.as_view(),name='detail_user'),
   path('category/', a.CategoryListView.as_view(),name='category'),
   path('category_field/', a.Category_Field_ListView.as_view(),name='category_field'),
   path('product/', a.ProductListView.as_view(),name='product'),
   path('product_image/', a.Product_image_ListView.as_view(),name='product_image'),
   path('signup/', a.Register.as_view()),
]