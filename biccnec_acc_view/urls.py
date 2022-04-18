from django.contrib import admin
from django.urls import path
from biccnec_view import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', views.authorization),
    path('api/v1/register/', views.registration),
]
