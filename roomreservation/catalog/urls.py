from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rentals/', views.RentalListView.as_view(), name='rentals'),
    path('rentals/<int:pk>', views.RentalDetailView.as_view(), name='rental-detail'),
]
