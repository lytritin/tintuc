"""vnegg_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from materials import views as materials_views
from courses import views
from profiles import views as profiles_views

from django.urls import path

from courses.views import ArticleDetailView

urlpatterns = [
    path('acp/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('material/', materials_views.home_material_view, name='material'),
    path('about/', views.about_view, name='about'),

    path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'),

    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', profiles_views.SiteLoginView.as_view(), name='login'),
    path('register/', profiles_views.SiteRegisterView.as_view(), name='register'),
    path('register/ok/', profiles_views.SiteRegisterOkView.as_view(), name='register_ok'),
    path('logout/', profiles_views.SiteLogoutView.as_view(), name='logout'),

    path('profile/', profiles_views.ProfileEditView.as_view(), name='profile'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
