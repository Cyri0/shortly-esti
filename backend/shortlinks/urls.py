from django.urls import path
from . import views

urlpatterns = [
    path('', views.short_urls),
    path('redirect/<int:id>/', views.short_url_redirect)
]