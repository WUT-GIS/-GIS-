from django.urls import path
from .views import UserRgisterView

urlpatterns = [
    path('register/', UserRgisterView.as_view(), name = 'register'),

]