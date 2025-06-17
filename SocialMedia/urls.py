from django.contrib import admin
from django.urls import path, include
from AppSocialMedia import views

urlpatterns = [
    path('', include('core.urls')),
    path('home/', include('river.urls')),
    path('search/', include('search.urls')),
    path('quacks/', include('quacks.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
