from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import render, redirect

from .models import VlogPost
from .forms import VlogPostForm, UserRegisterForm, UserLoginForm


# ------------------------------
# VLOG LIST VIEW
# ------------------------------
class VlogListView(LoginRequiredMixin, ListView):
    model = VlogPost
    template_name = 'vlogs/vlog_list.html'
    context_object_name = 'vlogs'
    paginate_by = 10
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VlogPostForm()
        return context


# ------------------------------
# VLOG DETAIL VIEW
# ------------------------------
class VlogDetailView(DetailView):
    model = VlogPost
    template_name = 'vlogs/vlog_detail.html'
    context_object_name = 'vlog'
    pk_url_kwarg = 'id'


# ------------------------------
# CREATE VLOG
# ------------------------------
class VlogCreateView(LoginRequiredMixin, CreateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = 'vlogs/vlog_form.html'
    success_url = reverse_lazy('vlog-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# ------------------------------
# UPDATE VLOG
# ------------------------------
class VlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = 'vlogs/vlog_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('vlog-list')

    def test_func(self):
        vlog = self.get_object()
        return vlog.author == self.request.user


# ------------------------------
# DELETE VLOG
# ------------------------------
class VlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VlogPost
    template_name = 'vlogs/vlog_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('vlog-list')

    def test_func(self):
        vlog = self.get_object()
        return vlog.author == self.request.user


# ------------------------------
# CUSTOM LOGIN VIEW
# ------------------------------
class CustomLoginView(LoginView):
    template_name = 'vlogs/login.html'
    authentication_form = UserLoginForm

    # Fix redirect so it never goes to /accounts/profile/
    def get_success_url(self):
        return reverse_lazy('vlog-list')


# ------------------------------
# CUSTOM LOGOUT VIEW
# ------------------------------
class CustomLogoutView(LogoutView):
    next_page = 'login'


# ------------------------------
# REGISTER VIEW
# ------------------------------
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'vlogs/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'vlogs/register.html', {'form': form})
