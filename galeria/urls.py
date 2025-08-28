from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('galeria/<int:id>/', views.pais_detail, name='pais_detail'),
    path('pesquisa/', views.pesquisar_pais, name='pesquisar_pais'),
]

