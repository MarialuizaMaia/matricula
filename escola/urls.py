from django.contrib import admin
from django.urls import path
from alunos.views import cadastrar_aluno, listar_alunos, editar_aluno, excluir_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_alunos, name='home'),
    path('cadastrar/', cadastrar_aluno, name='cadastrar'),
    path('editar/<int:pk>/', editar_aluno, name='editar'),
    path('excluir/<int:pk>/', excluir_aluno, name='excluir'),
]
