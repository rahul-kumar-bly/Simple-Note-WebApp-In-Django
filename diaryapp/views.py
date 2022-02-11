from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse_lazy
from . models import Note, ContactForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    FormView,
)
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# this is registration form
class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('note_list')
        return super(SignUpView, self).get(*args, **kwargs)

# this is login view
def login_user(request):
    if request.method == "POST":
            # check if user has correct credential
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username =username, password = password)
            if user is not None:
                login(request,user)
                return redirect('note_list')
            else:
                return redirect('/login')
    return render(request, "inout/login.html")

########################### Registration views end

#this is index page

def index(request):
    if request.user.is_anonymous:
        return redirect('login')        
    else:
        return redirect('note_list')

# this is note list view
class NoteListView(LoginRequiredMixin,ListView):
    template_name = "diaryapp/note_list.html"
    model = Note
    context_object_name = 'note_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note_list'] = context['note_list'].filter(user=self.request.user)        
       # search_note = self.request.GET.get('search_note')

        #if search_note:
         #   context['note_list'] = context['note_list'].filter(title__icontains = search_note)
          #  context['search_note'] = search_note 
        return context


# this is note detail view
class NoteDetailView(LoginRequiredMixin,DetailView):
    model = Note

# this is note create view
class NoteCreateView(LoginRequiredMixin,CreateView):
    template_name = "diaryapp/note_create.html"
    model = Note
    fields = ['title', 'message', 'image',]
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreateView, self).form_valid(form)

# this is note update view
class NoteUpdateView(UpdateView):
    template_name = "diaryapp/note_create.html"
    model = Note
    fields = ['title', 'message', 'image']
    success_url = reverse_lazy("note_list")

    def get_success_url(self):
        int_id = self.kwargs['pk']
        return reverse_lazy('note_detail', kwargs={'pk':int_id})

# this is note delete view
class NoteDeleteView(SuccessMessageMixin,DeleteView):
    template_name = "diaryapp/note_delete.html"
    model = Note
    success_url = reverse_lazy("note_list")





########################### Note views end


# this is contact form view
class ContactFormView(CreateView):
    template_name = "more/contact_us.html"
    model = ContactForm
    fields = ['name', 'message', 'email', 'phone']
    success_url = reverse_lazy('note_list')
