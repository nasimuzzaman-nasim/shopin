from django.urls import path
from account.api import views as aav

app_name = "register"

urlpatterns = [
    path('register/', aav.registration_view, name="register"),
    path('get-users/', aav.get_users_view, name="get-users")
]
