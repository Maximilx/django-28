from django.urls import path 
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('estudiante/<int:estudiante_id>', views.detalle_estudiantes, name ='detalle_estudiante' ),
]
