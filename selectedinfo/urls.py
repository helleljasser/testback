
from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_selected_text, name='save_selected_text'),
 
]
