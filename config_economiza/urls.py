"""config_economiza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from economiza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrar_home),
    path('home/', views.mostrar_home),
    path('cadastre/', views.mostrar_cadastre),
    path('cadastre/produto/', views.mostrar_cadastre_produto),
    path('cadastre/comercio/', views.mostrar_cadastre_comercio),
    path('minha-lista/', views.mostrar_minha_lista),
    path('minha-lista/novo-item/', views.mostrar_novo_item_lista),
    path('login/', views.mostrar_login),
    path('logout/submit', views.submit_logout),
    path('cadastro-usuario/', views.cadastre_usuario),
]
