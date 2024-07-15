"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, register_view
<<<<<<< HEAD
from cars.views import (CarDeleteView, CarDetailView, CarsListView,
                        CarUpdateView, NewCarCreateView)

urlpatterns = [
    path("admin/", admin.site.urls),
=======
from cars.views import CarsListView, NewCarCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", CarsListView.as_view(), name='cars_list'),
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),
    path("register/", register_view, name="register"),
>>>>>>> c67331d (Feat: Reescrevendo NewCarView como CreateView e testando.)
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("cars/", CarsListView.as_view(), name='cars_list'),
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car_update"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
