from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout, name='logout'),
    path('test/', test, name='test'),
    path('', HomeNews.as_view(), name ='home'),
    path('cat/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/',ViewNews.as_view(), name='view_news'),
    path('news/add-news>/', CreateNews.as_view(), name='add_news'),
]
