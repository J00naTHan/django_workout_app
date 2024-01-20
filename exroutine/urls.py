from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views


# URLS iniciais do site
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('app/', include('exassemble.urls'), name='app'),
    path('', RedirectView.as_view(url='app/', permanent=True), name='main'),
    path('accounts/register', views.register, name='register'),
    path('accounts/logout/', views.customLogout, name='cstm_logout'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
