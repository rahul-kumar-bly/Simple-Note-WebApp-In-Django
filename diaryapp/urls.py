from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name="home"),
    path('index/', login_required(views.NoteListView.as_view()), name="note_list"),
    path('note/<int:pk>', login_required(views.NoteDetailView.as_view()), name="note_detail"),
    path('create', login_required(views.NoteCreateView.as_view()), name="note_create"),
    path('note/<int:pk>/delete', login_required(views.NoteDeleteView.as_view()), name="note_delete"),
    path('note/<int:pk>/update', login_required(views.NoteUpdateView.as_view()),name="note_update"),
    path('contact/', views.ContactFormView.as_view(), name="contact"),
    path('login/', auth_view.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.SignUpView.as_view(), name="signup"),
]
