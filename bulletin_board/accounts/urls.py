from django.urls import path
from .views import ConfirmCode, LogIn, SignUp, logout_user

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('code/', ConfirmCode.as_view(), name='confirm_code'),
]
