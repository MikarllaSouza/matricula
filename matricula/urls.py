from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_aluno, name="listar_aluno"),
    path("cadastro/", views.criar_aluno, name="criar_aluno"), 
]