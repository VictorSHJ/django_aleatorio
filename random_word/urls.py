from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('generar/', views.index),
    path('reiniciar/', views.resetear)
]
