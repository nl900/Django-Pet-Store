from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('pets/', views.PetListView.as_view(), name='pets'),
        path('pet/<int:pk>', views.PetDetailView.as_view(), name='pet-detail'),
        path('breeders/', views.BreederListView.as_view(), name='breeders'),
        path('breeder/<int:pk>', views.BreederDetailView.as_view(), name='breeder-detail'),

]
