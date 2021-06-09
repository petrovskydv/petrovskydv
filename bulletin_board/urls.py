from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('cars/', views.CarList.as_view(), name='cars'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('cars/add/', views.CarCreateView.as_view(), name='cars-add'),
    path('cars/<int:pk>/edit/', views.CarUpdateView.as_view(), name='cars-update'),

    path('services/', views.ServiceList.as_view(), name='services'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='services-detail'),

    path('items/', views.PersonalItemList.as_view(), name='items'),
    path('items/<int:pk>/', views.PersonalItemDetailView.as_view(), name='items-detail'),

    path('accounts/profile/<int:pk>/', views.ProfileUpdate.as_view(), name='profile-update'),
]
