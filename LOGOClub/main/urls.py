from django.urls import path
from . import views 

urlpatterns = [
    path('aboutus', views.aboutus_render),
    path('contacts', views.contacts_render),
    path('logosad', views.logosad_render),
    path('serveses', views.serveses_render),
    path('states', views.states_render),
    path('', views.main_render),
]


