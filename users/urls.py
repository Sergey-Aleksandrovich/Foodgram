from django.urls import include, path

from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("signupsuccess/", views.SignupSuccess.as_view(), name="signup_success"),
    path('', include('django.contrib.auth.urls')),
]