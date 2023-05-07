from django.urls import path

from .views import AtividadeCreate, StatusCreate, ClasseCreate, ProgressaoCreate, CommentCreate, QuestionCreate
from .views import AtividadeUpdate, StatusUpdate, ClasseUpdate, ProgressaoUpdate, CommentUpdate, QuestionUpdate
from .views import AtividadeDelete, StatusDelete, ClasseDelete, ProgressaoDelete, CommentDelete, QuestionDelete
from .views import AtividadeList, StatusList, ClasseList, ProgressaoList, CommentList, QuestionList

urlpatterns = [
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),
    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name="cadastrar-progressao"),
    path('cadastrar/comentario', CommentCreate.as_view(), name='cadastrar-comentario'),
    path('cadastrar/question', QuestionCreate.as_view(), name='cadastrar-questao'),

    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/classe/<int:pk>', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/status/<int:pk>', StatusUpdate.as_view(), name='editar-status'),
    path('editar/progressao/<int:pk>', ProgressaoUpdate.as_view(), name='editar-progressao'),
    path('editar/comentario/<int:pk>', CommentUpdate.as_view(), name='editar-comentario'),
    path('editar/question/<int:pk>', QuestionUpdate.as_view(), name='editar-questao'),

    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name= 'excluir-atividade'),
    path('excluir/status/<int:pk>', StatusDelete.as_view(), name= 'excluir-status'),
    path('excluir/classe/<int:pk>', ClasseDelete.as_view(), name= 'excluir-classe'),
    path('excluir/progressao/<int:pk>', ProgressaoDelete.as_view(), name= 'excluir-progressao'),
    path('excluir/comentario/<int:pk>', CommentDelete.as_view(), name='excluir-comentario'),
    path('excluir/question/<int:pk>', QuestionDelete.as_view(), name='excluir-questao'),

    path('listar/atividades/', AtividadeList.as_view(), name= 'listar-atividades'),
    path('listar/status/', StatusList.as_view(), name= 'listar-status'),
    path('listar/classes/', ClasseList.as_view(), name= 'listar-classes'),
    path('listar/progressao/', ProgressaoList.as_view(), name='listar-progressao'),
    path('listar/comentario/', CommentList.as_view(), name='listar-comentario'),
    path('listar/question/', QuestionList.as_view(), name='listar-questao'),
]