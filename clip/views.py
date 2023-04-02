from django.shortcuts import render, redirect, reverse
from .models import Clip, User, Episode
from .forms import RegisterFrom, HomeForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class HomePage(FormView):
    template_name = 'index.html'
    form_class = HomeForm


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
    
            return redirect('clip:homeclips')
        else:
            return super().get(request, *args, **kwargs)
        


    def get_success_url(self):
        email = self.request.POST.get('email')
        user = User.objects.filter(email=email)

        if user:
            return reverse('clip:login')
        else:
            return reverse('clip:register')
    


class HomeClips(LoginRequiredMixin, ListView):
    template_name = 'homeclips.html'
    model = Clip
 

class DetailsClips(LoginRequiredMixin, DetailView):
    template_name = 'detailsclips.html'
    model = Clip


    def get(self, request, *args, **kwargs):
        episode = self.get_object()
        episode.views += 1
        episode.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailsClips, self).get_context_data(**kwargs)


        return context
    

class SearchClip(LoginRequiredMixin, ListView):
    template_name = 'search.html'
    model = Clip

    def get_queryset(self):
        search_request = self.request.GET.get('q')
        if search_request:
            object_list = self.model.objects.filter(title__icontains=search_request)
            
            return object_list
       
        else:
            return None
       
   

class EditProfile(LoginRequiredMixin, UpdateView):
    template_name = 'editprofile.html'
    model = User
    fields = ['first_name', 'last_name' , 'email']


    def get_success_url(self):
        return reverse('clip:homeclips')


class Register(FormView):
    template_name = 'register.html'
    form_class = RegisterFrom

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    def get_sucess_url(self):

        return reverse('clip:login')
