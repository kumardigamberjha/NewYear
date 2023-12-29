from django.urls import path
from red import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('HandleQRCode/<str:mobile>/', views.handle_qr_scan, name="handle_qr_code"),
    path('CheckQRCode/<str:mobile>/', views.Check_qr_scan, name="check_qr_code"),


]
