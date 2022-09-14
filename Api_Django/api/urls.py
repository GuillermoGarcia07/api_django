from django.urls import path
from .views import alumnosView

urlpatterns = [
    path('alumnos/', alumnosView.as_view(), name= 'alumnos_list'),
]