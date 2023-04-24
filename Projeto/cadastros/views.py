from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade, Campus, Status, Classe, Comprovante, Progressao, Validacao

from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin


from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404


class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Campo"
        context['botao'] = "Cadastrar"

        return context


class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Atividade"
        context['botao'] = "Cadastrar"

        return context


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


class CampusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Campus"
        context['botao'] = "Cadastrar"

        return context


class ComprovanteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-comprovante')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Campus"
        context['botao'] = "Cadastrar"

        return context
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)  # antes do super o objeto n foi criado
        return url



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


class ValidacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Validacao
    readonly_fields = ['validado_em']
    fields = ['comprovante',
              'validado_por', 'quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Campus"
        context['botao'] = "Cadastrar"

        return context

# Update


class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Campo"
        context['botao'] = "Salvar"

        return context


class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
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


class CampusUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Campus"
        context['botao'] = "Salvar"
        context['icon'] = '<i class="bi bi-check"></i>'
        return context


class ComprovanteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-comprovante')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Comprovante"
        context['botao'] = "Salvar"

        return context
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Comprovante, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


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


class ValidacaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Validacao
    fields = ['comprovante', 'validado_em',
              'validado_por', 'quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Editar cadastro de Validação"
        context['botao'] = "Salvar"
        context['icon'] = "<i class='bi bi-check'></i>"

        return context

# Delete


class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')


class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')


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


class CampusDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Campus
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campus')
    


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


class ValidacaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Validacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-validacao')

# list


class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = "cadastros/listas/campo.html"


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


class CampusList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campus
    template_name = "cadastros/listas/campus.html"
    paginate_by = 10

    def get_queryset(self):
        txt_cidade = self.request.GET.get('cidade')

        if txt_cidade:
            campi = Campus.objects.filter(cidade__icontains=txt_cidade) 
        else:
            campi = Campus.objects.all()
        return campi


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


class ValidacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Validacao
    template_name = "cadastros/listas/validacao.html"

