# from django.urls import path
#
# from apps.auth.views import UserCreateView
#
# urlpatterns = [
#     path('register.html/', UserCreateView.as_view(), name='register.html'),
# ]


from django.contrib.auth.views import LoginView
from django.urls import path

from apps.users.views import (
    UserCreateView, UserDetailView, UserUpdateView, UserDeleteView, RegisterView, logout_view, UserProfileView, HomeView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('auth/login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('auth/profile/', UserProfileView.as_view(), name='user_profile'),
    path('auth/logout/', logout_view, name='logout'),
    path('users/list/', UserCreateView.as_view(), name='user_list'),
    path('users/detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]





