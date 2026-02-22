from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mark-attendance/<int:subject_id>/', views.mark_attendance, name='mark_attendance'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]