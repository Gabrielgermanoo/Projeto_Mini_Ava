from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group
from .forms import UsuarioForm
from .models import Perfil

from django.shortcuts import get_object_or_404

# Create your models here.

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):

        grupo = get_object_or_404(Group, name = 'Comum')
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario = self.object)
        
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Registrar novo usuário"
        context['botao'] = "Registrar"
        context['icon'] = '<i class="bi bi-check"></i>'

        return context

class PerfilUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('index')

    def get_object(self, queryset = None):
        self.object = get_object_or_404(Perfil, usuario = self.request.user)
        return self.object

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Meus dados pessoais"
        context['botao'] = "Atualizar"
        context['icon'] = '<i class="bi bi-check"></i>'

        return context