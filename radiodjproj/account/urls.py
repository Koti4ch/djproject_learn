from django.urls import path
from django.contrib.auth import views as authviews
from account import views as accountviews
app_name = 'account'


urlpatterns = [
    # path('login/', accountviews.user_login, name='user_login'),
    path('login/', authviews.LoginView.as_view(template_name='registration/user_login.html'), name='user_login'),
    path('logout/', authviews.LogoutView.as_view(template_name='registration/user_logged_out.html'), name='user_logout'),
    path('', accountviews.dashboard, name='dashboard'),
]