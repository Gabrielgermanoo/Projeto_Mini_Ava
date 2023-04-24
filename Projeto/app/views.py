from django.views.generic import TemplateView

class indexView(TemplateView):
    template_name = "paginas/index.html"

class sobreView(TemplateView):
    template_name = 'paginas/about.html'

