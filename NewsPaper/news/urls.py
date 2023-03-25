from django.urls import path
from .views import PostList, PostDetail#, CategoryList

urlpatterns = [

    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    #path('', CategoryList.as_view())
    ]
