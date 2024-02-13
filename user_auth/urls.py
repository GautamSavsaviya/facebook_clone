from django.urls import path
from . import views

app_name = "user_auth"

urlpatterns = [
    path("sign-up/", views.register_user, name='sign-up'),
]
