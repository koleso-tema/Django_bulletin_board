from django.urls import path
from .views import *

urlpatterns = [
    path('home/', AnnoList.as_view(), name='anno_list'),
    path('home/<int:pk>/', AnnoDetail.as_view(), name='anno_detail'),
    path('personal_area/', PersonalArea.as_view(), name='personal_area'),
    path('personal_area/create/', AnnoCreate.as_view(), name='anno_create'),
    path('personal_area/<int:pk>/response/', ResponseCreate.as_view(), name='response_create'),
    path('home/<int:pk>/response/<int:id>/', accept_response, name='accept_response'),
    path('home/<int:pk>/response/<int:id>/', cancel_response, name='cancel_response'),
    path('home/<int:pk>/update/', AnnoUpdate.as_view(), name='anno_update'),
    path('home/<int:pk>/delete/', AnnoDelete.as_view(), name='anno_delete'),
    path('response/<int:pk>/update/', ResponseUpdate.as_view(), name='response_update'),
    path('response/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete'),


]