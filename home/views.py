from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class indexView(TemplateView):
    template_name = "home/index.html"

#def index(request):
    #return render(request, 'home/index.html')


class aboutView(TemplateView):
    template_name = "home/about.html"
#def about(request):
    #return render(request, 'home/about.html')


class contactView(SuccessMessageMixin, FormView):
    template_name = "home/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')#işlem tamamlandıktan sonra contact sayfasına tekrar yönlendirilir.
    success_message = 'We received your request'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)#ilgili form kaydedilir.
#def contact(request):
    #return render(request, 'home/contact.html')


class loginView(TemplateView):
    template_name = "home/login.html"
#def login(request):
    #return render(request, 'home/login.html')
