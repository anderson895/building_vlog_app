from django.urls import path
from .views import (
    VlogListView, VlogDetailView, VlogCreateView,
    VlogUpdateView, VlogDeleteView,
    CustomLoginView, CustomLogoutView, RegisterView
)

urlpatterns = [
    # Vlog routes
    path('', VlogListView.as_view(), name='vlog-list'),
    path('vlog/<int:id>/', VlogDetailView.as_view(), name='vlog-detail'),
    path('vlog/new/', VlogCreateView.as_view(), name='vlog-create'),
    path('vlog/edit/<int:id>/', VlogUpdateView.as_view(), name='vlog-edit'),
    path('vlog/delete/<int:id>/', VlogDeleteView.as_view(), name='vlog-delete'),

    # Auth routes
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
