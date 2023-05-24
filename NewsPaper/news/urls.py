from django.urls import path
from .views import PostList, PostDetail, multiply, PostCreate, PostUpdate, PostDelete, PostSearch, CommentPost, CategoryListView, subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    # path('multiply/', multiply),
    path('search/', PostSearch.as_view()),
    path('create/', PostCreate.as_view(), name='post_edit'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/comment/', CommentPost.as_view(), name='comment'),
    path('categories/<int:pk>', cache_page(900)(CategoryListView.as_view()), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]
