from django.urls import path,include
from test_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .forms import LoginForm,MyPasswordResetForm,MySetPasswordForm
#from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView,TokenVerifyView



urlpatterns = [
path('', views.user_Dashboard, name='dashboard'),

    # Login,Logout authentication
path('register', views.user_registration, name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #     Forgot password

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='ResetPassword/password_reset.html',
                                              form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='ResetPassword/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='ResetPassword/password_reset_confirm.html',
                                                     form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='ResetPassword/password_reset_complete.html'),
         name='password_reset_complete'),


#     API url
    path('api/', include('test_app.routers')),

#     JWT Url
#    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
  #  path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
  #  path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
    # path('refreshtoken/'TokenRefreshView.as_view(),name='token_refresh')
    # path('veifytoken/'TokenVerifyView.as_view(),name='token_refresh')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


