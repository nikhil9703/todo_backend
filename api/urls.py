
from django.urls import path
from .views import signup, login, HomeView, sent_reset_email, reset_password, task_list_create, task_detail

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path("password-reset/", sent_reset_email, name="password_reset"),
    path("password-reset-confirm/<uidb64>/<token>/", reset_password, name="password_reset_confirm"),
    path('tasks/', task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),
]