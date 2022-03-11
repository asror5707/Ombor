
from django.contrib import admin
from django.urls import path

from ombor_app.views import ProductAPIView, OmborAPIView,ClientAPIView,ProductRUD, OmborRUD,ClientRUD
from rest_framework.authtoken.views import obtain_auth_token
from staticapp.views import StatsAPIView, StatsRUD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', ClientAPIView.as_view()),
    path('client/<int:pk>/', ClientRUD.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductRUD.as_view()),
    path('ombor/', OmborAPIView.as_view()),
    path('ombor/<int:pk>/', OmborRUD.as_view()),
    path('stats/', StatsAPIView.as_view()),
    path('stats/<int:pk>/', StatsRUD.as_view()),
    path('get-token/', obtain_auth_token),
]
