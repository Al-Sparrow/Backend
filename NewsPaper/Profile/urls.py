from django.urls import path
from .views import UserUpdate, upgrade_me, UserInfo

urlpatterns = [
    path('<int:pk>', UserInfo.as_view(), name='accounts_info'),
    path('<int:pk>/update_profile/', UserUpdate.as_view(), name = 'accounts_update'),
    path('<int:pk>/update_profile/upgrade/', upgrade_me, name = 'upgrade'),
]