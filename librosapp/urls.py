from django.urls import path
from . import views
from .views import LibroList, New, LibroDetalle

urlpatterns = [
    path('',LibroList.as_view(), name='libro_list'),
    path('new',New.as_view(), name='new'),
    path('libro/<int:pk>/',LibroDetalle.as_view(), name='libro_details'),
]