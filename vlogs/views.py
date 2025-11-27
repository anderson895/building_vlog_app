# vlogs/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from .models import VlogPost
from .forms import VlogPostForm, UserRegisterForm, UserLoginForm

# List view
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

# Detail view
class VlogDetailView(DetailView):
    model = VlogPost
    template_name = 'vlogs/vlog_detail.html'
    context_object_name = 'vlog'
    pk_url_kwarg = 'id'

# Create view
class VlogCreateView(LoginRequiredMixin, CreateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = 'vlogs/vlog_form.html'
    success_url = reverse_lazy('vlog-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update view
class VlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = 'vlogs/vlog_form.html'
    success_url = reverse_lazy('vlog-list')
    pk_url_kwarg = 'id'

    def test_func(self):
        vlog = self.get_object()
        return self.request.user == vlog.author

# Delete view
class VlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VlogPost
    template_name = 'vlogs/vlog_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('vlog-list')

    def test_func(self):
        vlog = self.get_object()
        return self.request.user == vlog.author

# User registration/login views
class UserRegisterView(FormView):
    template_name = 'vlogs/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'vlogs/login.html'
    authentication_form = UserLoginForm

# vlogs/views.py
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('vlog-list')
    allow_get = True  # <-- Add this to allow GET requests
