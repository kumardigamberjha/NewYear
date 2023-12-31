from django.urls import path
from red import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('HandleQRCode/<str:mobile>/', views.handle_qr_scan, name="handle_qr_code"),
    path('ActivateQRCode/<str:mobile>/', views.Activate_QR_scan, name="activate_qr_code"),

    path('CheckQRCode/<str:mobile>/', views.Check_qr_scan, name="check_qr_code"),
    path('RemoveQrCode/<str:mobile>/', views.Remove_QR_SCAN, name="remove_qr_code"),

    # path('DeleteQRCode/', views.Del_All_QR_SCAN, name="del_all_qr_code"),

    path('AllRecords/', views.CheckInvitations, name="checkinvite"),
    path('CheckOut/', views.CheckOut, name="checkout"),
    path('login/', views.login_view, name='login'),
]
