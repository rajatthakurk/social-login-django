from django.contrib import admin
from django.urls import path, include
# from .views import Home,dashboard
from .views import home,dashboard


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dashboard", dashboard, name="dashboard"),
    path("", home, name="home"),
    path("crud/", include("crud_app.urls")),

    # path('dashboard',dashboard,name='dashboard')
]