from django.urls import path
from . import views
urlpatterns = [
    path('',views.view_login_page),
    path('verify/',views.show),
    path('signup1/',views.signup_screen1),
    path('forgot1/',views.forgot_screen1),
    path('forgot2/',views.forgot_screen2),
    path('reset/',views.verify_otp),
    path('reset2/',views.reset_password),
    path('signup!4/',views.signup_screen4),
    path('verifyemail/',views.send_otp),
    path('signup3/',views.verify_otp1),
    path('signup4/',views.check_user),
    path('test1/',views.show2)

]