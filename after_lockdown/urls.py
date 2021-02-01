"""after_lockdown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from front_end import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('validate/',views.validate,name='validate'),
    path('',TemplateView.as_view(template_name='log_in.html'),name='log_in'),
    path('hm',views.hm, name='hm'),
    path('verification_page/',views.verification_page, name='verification_page'),
    path('verification/',views.verification, name='verification'),
    path('update/<int:id>/',views.update,name='update'),
    path('save/<int:id>/',views.save, name='save'),
    path('log_out/',views.log_out, name='log_out'),
    path('add_new_user/',views.add_new_user, name='add_new_user'),
    path('admin_hm/',views.admin_hm, name='admin_hm'),
    # path('search/',views.search, name='search')

]
