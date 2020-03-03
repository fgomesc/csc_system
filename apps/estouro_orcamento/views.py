from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.centro_de_custo.models import CentroDeCusto
from apps.usuario.models import Usuario
from .forms import CadastroEstouroOrcamento, CadastroEstouroForm

""" <<<<<< Estouro de Verba - Cadastro

Criando Estouro de Orçamento

Parte aonde o usuário lançador ira criar os estouros de orçamento

"""

class CadastroEstouroList(LoginRequiredMixin, ListView):
    model = CadastroEstouroOrcamento

    def get_queryset(self):
        print(self.request.user.pk)
        centros = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return CadastroEstouroOrcamento.objects.filter(cc_cadastro_orcamento__in=centros)



class CadastroEstouroEdit(LoginRequiredMixin, UpdateView):
    model = CadastroEstouroOrcamento
    form_class = CadastroEstouroForm

    def get_form_kwargs(self):
        kwargs = super(CadastroEstouroEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class CadastroEstouroDelete(LoginRequiredMixin, DeleteView):
    model = CadastroEstouroOrcamento
    success_url = reverse_lazy('list_cadastro_estouro')



class CadastroEstouroCreate(LoginRequiredMixin, CreateView):
    model = CadastroEstouroOrcamento
    form_class = CadastroEstouroForm

    def get_form_kwargs(self):
        kwargs = super(CadastroEstouroCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



"""

class AprovarEstouroList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CadastroOrcamento
    permission_required = 'can_see_aprove_orcamento'
    template_name = 'cadastro_orcamento/aprovar_orcamento_list.html'


    def get_queryset(self):
        print(self.request.user.pk)
        orcamentos = Usuario.objects.filter(user__pk=self.request.user.pk).first().centrodecusto_usuario.all()
        return CadastroOrcamento.objects.filter(aprovacao=False)



class AprovadorOrcamentoEdit(UpdateView):
    model = CadastroOrcamento
    fields = ['valor_cadastro_orcamento', 'obs_cadastro_orcamento', 'aprovacao']
    success_url = reverse_lazy('list_aprovar_estouro')
    

"""


def load_naturezas(request):
    centro_id = request.GET.get('centro')
    centro = CentroDeCusto.objects.filter(pk=centro_id).first()
    naturezas = centro.vinculo_natureza.all()

    return render(request, 'estouro_orcamento/naturezas_list_options.html', {'naturezas': naturezas})
