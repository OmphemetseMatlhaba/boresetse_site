from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
    path('principal-message/', views.principal_message),
    path('payments/', views.payments),
    path('mural-activities/', views.mural_activities),
    path('top-students/', views.top_students),
    path('staff-sgb/', views.staff_sgb),
    path('newsletter/', views.newsletter),
]   