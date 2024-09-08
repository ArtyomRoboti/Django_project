from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def view_func(request):
    return render(request, 'func_view.html')

class ClassView(TemplateView):
    template_name = 'class_view.html'