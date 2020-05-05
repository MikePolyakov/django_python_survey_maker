from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView


from .models import Structure, Company


# Create your views here.
def main_view(request):
    pass
    return render(request, 'constructor_app/index.html', context={})


def companies_view(request):
    companies = Company.objects.all()
    return render(request, 'constructor_app/companies.html', context={'companies': companies})


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
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('constructor:index'))

        else:
            return render(request, 'constructor_app/landing.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'constructor_app/landing.html', context={'form': form})


def show_structure(request):
    pass
    return render(request, 'constructor_app/structure.html', {'department': Structure.objects.all()})


class CompaniesListView(ListView):
    # model = Article
    # queryset = Company.objects.select_related('user').all()
    queryset = Company.objects.all()
    template_name = 'constructor_app/companies.html'
    # ordering = ['-date']
    # paginate_by = 5
    # если хотим изменить имя  object_list
    # context_object_name = 'news_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['count'] = 4
        return context


# DetailView для поста
# class CompanyDetailView(UserPassesTestMixin, DetailView):
#     # queryset = Company.objects.select_related('user').all()
#     queryset = Company.objects.get(id=id)
#     template_name = 'constructor/company_details.html'
#
#     def test_func(self):
#         return self.request.user.is_superuser
#
#     def handle_no_permission(self):
#         return redirect('users:login')
#
#     def get(self, request, *args, **kwargs):
#         self.company_id = kwargs['pk']
#         return super().get(request, *args, **kwargs)
#
#     def get_object(self):
#         return get_object_or_404(Company, pk=self.company_id)

def company(request, id):
    company = get_object_or_404(Company, id=id)
    company = Company.objects.get(id=id)
    return render(request, 'constructor_app/company.html', context={'company': company})



# CreateView for article
# class CompanyCreateView(CreateView):
#     # form_class =
#     queryset = Company.objects.select_related('source')
#     fields = ('name', 'url', 'source')
#     # model = Article
#     # fields = '__all__'
#     success_url = reverse_lazy('covid_19:news')
#     template_name = 'constructor_app/add_company.html'
#
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         return super().form_valid(form)


# добавление company
class CompanyCreateView(CreateView):
    fields = '__all__'
    model = Company
    success_url = reverse_lazy('survey_maker:company')
    template_name = 'constructor_app/add_company.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)