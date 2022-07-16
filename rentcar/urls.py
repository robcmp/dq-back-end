from django.urls import path
from .views import ClientAPIView, CompanyAPIView

urlpatterns = [
    path('api/client/', ClientAPIView.as_view()),
    path('api/company/', CompanyAPIView.as_view())
]
