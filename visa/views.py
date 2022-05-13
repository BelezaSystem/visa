from django.views.generic import TemplateView
from .models import Atividades
from .busca_api import pega_resultado


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['atividades'] = Atividades.objects.all()

        return context


class CnpjView(TemplateView):
    template_name = 'cnpj.html'

    def get_context_data(self, **kwargs):
        context = super(CnpjView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        context['atividades'] = ''
        if search:
            cnaelist = pega_resultado(search)
            context['atividades'] = Atividades.objects.filter(cnae__in=cnaelist)

            if type(cnaelist) == str:
                context['atividades'] = "vazio"

        return context
