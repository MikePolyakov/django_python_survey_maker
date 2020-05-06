from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView


from .models import Structure, Company


# Create your views here.
def landing_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                'Contact message',
                f'Ваш сообщение "{subject}" принято',
                'id2k1149@gmail.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('constructor:index'))

        else:
            return render(request, 'constructor_app/landing.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'constructor_app/landing.html', context={'form': form})


# ListView
class CompaniesListView(ListView):
    model = Company
    template_name = 'constructor_app/companies.html'


# DetailView
class CompanyDetailView(DetailView):
    model = Company
    template_name = 'constructor_app/company.html'


# CreateView
class CompanyCreateView(CreateView):
    fields = ('name',)
    model = Company
    success_url = reverse_lazy('constructor:companies')
    template_name = 'constructor_app/create.html'

    # def someview(request):
    #     form = SomeForm(..)
    #
    #     if some_condition:
    #         name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))
    #         form.fields['email'].widget.attrs['placeholder'] = instance.email

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)
