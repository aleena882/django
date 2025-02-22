"""
URL configuration for bookcreation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from bookcard import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.books),
    path('cards/', views.dis_book),
    path('book_search/', views.book_search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("delete/<int:id>", views.delete),
    path("update/<int:id>", views.update)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

