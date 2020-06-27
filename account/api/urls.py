from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from account.api import views as aav

app_name = "register"

urlpatterns = [
    path('register/', aav.registration_view, name="register"),
    path('get-users/', aav.get_users_view, name="get-users"),
    path('login/', obtain_auth_token, name="login"),
]
