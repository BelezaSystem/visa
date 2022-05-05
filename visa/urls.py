from django.urls import path
from .views import IndexView, CnpjView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'visa'

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('consulta_cnpj/', CnpjView.as_view(), name='consulta_cnpj'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
