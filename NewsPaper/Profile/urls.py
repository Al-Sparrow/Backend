from django.urls import path, include
from .views import UserUpdate, upgrade_me, UserInfo

urlpatterns = [
    path('<int:pk>/', include([
        path('', UserInfo.as_view(), name = 'accounts_info'),
        path('upgrade/', upgrade_me, name = 'upgrade'),
        path('update_profile/', UserUpdate.as_view(), name = 'accounts_update')]))
]