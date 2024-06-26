from django.urls import path
from .views import SignupView, CLoginView, ChangeUserView,settings


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", CLoginView.as_view(), name="login"),
    path("<int:pk>/edit/", ChangeUserView.as_view(), name="edit_profile"),
    path("",settings,name="accounts_settings")
]
