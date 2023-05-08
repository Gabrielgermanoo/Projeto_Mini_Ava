from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Atividade, Status, Classe, Comprovante, Progressao, Comment, Question

from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django import forms


from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404

class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Atividade"
        context['botao'] = "Cadastrar"

        return context
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # antes do super o objeto n foi criado
        return url
    


class StatusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Status"
        context['botao'] = "Cadastrar"

        return context


class ClasseCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Classe"
        context['botao'] = "Cadastrar"

        return context

class ProgressaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Campus"
        context['botao'] = "Cadastrar"

        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # antes do super o objeto n foi criado
        self.object.observacao += " (Observation)"
        self.object.save()
        return url

class CommentCreate(CreateView):
    model = Comment
    fields = ['body']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Adicionar comentário"
        context['botao'] = "Comentar"

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # antes do super o objeto n foi criado
        self.object.save()
        return url
    
class QuestionCreate (CreateView):
    model = Comment
    fields = ['body']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Adicionar questão"
        context['botao'] = "Enviar"

        return context
    

# Update

class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Atividade"
        context['botao'] = "Salvar"

        return context

class StatusUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Status"
        context['botao'] = "Salvar"

        return context


class ClasseUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Classe"
        context['botao'] = "Salvar"

        return context


class ProgressaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Progressão"
        context['botao'] = "Salvar"
        context['icon'] = "<i class='bi bi-check'></i>"

        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Progressao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class CommentUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Comment
    fields = ['body']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar Comentário"
        context['botao'] = "Salvar"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Comment, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class QuestionUpdate(UpdateView):
    login_url = reverse_lazy('login')
    model = Question
    fields = ['body']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-questoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar Questão"
        context['botao'] = "Salvar"

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Question, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

# Delete

class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.Form() # replace with your actual form
        return context


class StatusDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-status')


class ClasseDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classes')

class ComprovanteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Comprovante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comprovante')


class ProgressaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Progressao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-progressao')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Progressao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CommentDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Comment
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comentario')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Comment, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class QuestionDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Question
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-questao')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Question, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

# list

class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = "cadastros/listas/atividade.html"


class StatusList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Status
    template_name = "cadastros/listas/status.html"


class ClasseList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = "cadastros/listas/classe.html"

class ComprovanteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Comprovante
    template_name = "cadastros/listas/comprovante.html"

    def get_queryset(self):
        self.object_list = Comprovante.objects.filter(usuario=self.request.user)
        return self.object_list


class ProgressaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Progressao
    template_name = "cadastros/listas/progressao.html"

    # filtro de progressao de usuarios individual
    def get_queryset(self):
        self.object_list = Progressao.objects.filter(usuario=self.request.user)
        return self.object_list

class CommentList(ListView):
    login_url = reverse_lazy('login')
    model = Comment
    template_name = 'cadastros/listas/comentario.html'

    def get_queryset(self):
        self.object_list = Comment.objects.filter(usuario=self.request.user)
        return self.object_list
    
class QuestionList(ListView):
    login_url = reverse_lazy('login')
    model = Question
    template_name = 'cadastros/listas/enquete.html'

    def get_queryset(self):
        self.object_list = Question.objects.filter(usuario=self.request.user)
        return self.object_list