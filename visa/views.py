from django.views.generic import TemplateView
from .models import Atividades
from .busca_api import pega_resultado


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        option = self.request.GET.get('options')

        if not search:
            context['atividades'] = Atividades.objects.all()
        else:
            if option == 'cnae':

                context['atividades'] = Atividades.objects.filter(cnae=search)  # busca exata por cnae
            elif option == 'atividade':
                context['atividades'] = Atividades.objects.filter(atividade__icontains=search)  # busca por string
        return context


class CnpjView(TemplateView):
    template_name = 'cnpj.html'

    def get_context_data(self, **kwargs):
        ''' varivarel para testes
        cod = ['47.44-0-99', '45.30-7-03', '47.41-5-00', '47.42-3-00',
               '47.43-1-00', '47.44-0-01', '47.53-9-00', '47.54-7-01',
               '47.54-7-03', '49.30-2-01', '49.30-2-02', '77.19-5-99',
               '77.32-2-01', '43.19-3-00', '43.11-8-02']'''

        context = super(CnpjView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        context['atividades'] = ''
        if search:
            cnaelist = pega_resultado(search)
            context['atividades'] = Atividades.objects.filter(cnae__in=cnaelist)

            if type(cnaelist) == str:
                context['atividades'] = "vazio"

        return context
