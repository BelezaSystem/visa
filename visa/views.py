from django.views.generic import TemplateView
from .models import Atividades, Perguntas


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        option = self.request.GET.get('options')

        if search:
            if option == 'cnae':
                context['atividades'] = Atividades.objects.filter(cnae=search)  # busca exata por cnae
            elif option == 'atividade':
                context['atividades'] = Atividades.objects.filter(atividade__istartswith=search)  # busca por string
            else:
                context['atividades'] = Atividades.objects.all()
        return context


class CnpjView(TemplateView):
    template_name = 'cnpj.html'

    def get_context_data(self, **kwargs):
        context = super(CnpjView, self).get_context_data(**kwargs)
        context['atividades'] = Atividades.objects.all()
        return context
