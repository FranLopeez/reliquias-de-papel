from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DetailView
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileForm
from .models import Profile



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user.profile


