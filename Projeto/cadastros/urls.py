from django.urls import path

from .views import CampoCreate, AtividadeCreate, StatusCreate, ClasseCreate, CampusCreate, ComprovanteCreate, ProgressaoCreate, ValidacaoCreate
from .views import CampoUpdate, AtividadeUpdate, StatusUpdate, ClasseUpdate, CampusUpdate, ComprovanteUpdate, ProgressaoUpdate, ValidacaoUpdate
from .views import CampoDelete, AtividadeDelete, StatusDelete, ClasseDelete, CampusDelete, ComprovanteDelete, ProgressaoDelete, ValidacaoDelete
from .views import CampoList, AtividadeList, StatusList, ClasseList, CampusList, ComprovanteList, ProgressaoList, ValidacaoList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('cadastrar/campus/', CampusCreate.as_view(), name="cadastrar-campus"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),
    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/comprovante/', ComprovanteCreate.as_view(), name="cadastrar-comprovante"),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name="cadastrar-progressao"),
    path('cadastrar/validacao/', ValidacaoCreate.as_view(), name="cadastrar-validacao"),

    path('editar/campo/<int:pk>', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),
    path('editar/campus/<int:pk>', CampusUpdate.as_view(), name='editar-campus'),
    path('editar/classe/<int:pk>', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/status/<int:pk>', StatusUpdate.as_view(), name='editar-status'),
    path('editar/comprovante/<int:pk>', ComprovanteUpdate.as_view(), name='editar-comprovante'),
    path('editar/progressao/<int:pk>', ProgressaoUpdate.as_view(), name='editar-progressao'),
    path('editar/validacao/<int:pk>', ValidacaoUpdate.as_view(), name='editar-validacao'),

    path('excluir/campo/<int:pk>', CampoDelete.as_view(), name= 'excluir-campo'),
    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name= 'excluir-atividade'),
    path('excluir/status/<int:pk>', StatusDelete.as_view(), name= 'excluir-status'),
    path('excluir/classe/<int:pk>', ClasseDelete.as_view(), name= 'excluir-classe'),
    path('excluir/campus/<int:pk>', CampusDelete.as_view(), name= 'excluir-campus'),
    path('excluir/comprovante/<int:pk>', ComprovanteDelete.as_view(), name= 'excluir-comprovante'),
    path('excluir/progressao/<int:pk>', ProgressaoDelete.as_view(), name= 'excluir-progressao'),
    path('excluir/validacao/<int:pk>', ValidacaoDelete.as_view(), name= 'excluir-validacao'),

    path('listar/campos/', CampoList.as_view(), name= 'listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name= 'listar-atividades'),
    path('listar/status/', StatusList.as_view(), name= 'listar-status'),
    path('listar/classes/', ClasseList.as_view(), name= 'listar-classes'),
    path('listar/campus/', CampusList.as_view(), name= 'listar-campus'),
    path('listar/comprovante/', ComprovanteList.as_view(), name= 'listar-comprovante'),
    path('listar/progressao/', ProgressaoList.as_view(), name= 'listar-progressao'),
    path('listar/validacao/', ValidacaoList.as_view(), name= 'listar-validacao'),
]