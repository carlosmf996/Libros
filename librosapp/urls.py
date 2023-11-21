from django.urls import path
from . import views
from .views import LibroList, New, LibroDetalle, Edit, Delete

urlpatterns = [
    path('',LibroList.as_view(), name='libro_list'),
    path('new',New.as_view(), name='new'),
    path('libro/<int:pk>/',LibroDetalle.as_view(), name='libro_details'),
    path('libro/<int:pk>/edit/', Edit.as_view(), name='libro_edit'),
    path('libro/<int:pk>/delete/', Delete.as_view(), name='libro_delete'),
]