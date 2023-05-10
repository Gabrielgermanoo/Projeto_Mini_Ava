from django.urls import path

from .views import AtividadeCreate, StatusCreate, ClasseCreate, ProgressaoCreate, CommentCreate
from .views import AtividadeUpdate, StatusUpdate, ClasseUpdate, ProgressaoUpdate, CommentUpdate
from .views import AtividadeDelete, StatusDelete, ClasseDelete, ProgressaoDelete, CommentDelete
from .views import AtividadeList, StatusList, ClasseList, ProgressaoList, CommentList

urlpatterns = [
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),
    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name="cadastrar-progressao"),
    path('cadastrar/questao', CommentCreate.as_view(), name='cadastrar-questao'),

    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/classe/<int:pk>', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/status/<int:pk>', StatusUpdate.as_view(), name='editar-status'),
    path('editar/progressao/<int:pk>', ProgressaoUpdate.as_view(), name='editar-progressao'),
    path('editar/questao/<int:pk>', CommentUpdate.as_view(), name='editar-questao'),

    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name= 'excluir-atividade'),
    path('excluir/status/<int:pk>', StatusDelete.as_view(), name= 'excluir-status'),
    path('excluir/classe/<int:pk>', ClasseDelete.as_view(), name= 'excluir-classe'),
    path('excluir/progressao/<int:pk>', ProgressaoDelete.as_view(), name= 'excluir-progressao'),
    path('excluir/questao/<int:pk>', CommentDelete.as_view(), name='excluir-comentario'),

    path('listar/atividades/', AtividadeList.as_view(), name= 'listar-atividades'),
    path('listar/status/', StatusList.as_view(), name= 'listar-status'),
    path('listar/classes/', ClasseList.as_view(), name= 'listar-classes'),
    path('listar/progressao/', ProgressaoList.as_view(), name='listar-progressao'),
    path('listar/questao/', CommentList.as_view(), name='listar-questao'),
]