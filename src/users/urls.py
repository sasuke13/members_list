from django.urls import path

from users.views import UserAPIView

urlpatterns = [
    path('', UserAPIView.as_view(), name='get_all_users_or_create_user'),
    path('<int:id>/', UserAPIView.as_view(), name='get_user_by_id')
]
