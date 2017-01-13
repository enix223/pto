import json
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import (authenticate, login, logout)
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm, PtoRequestForm
from accounts.models import PtoHistory



class IndexView(FormView):
    template_name = 'accounts/index.html'
    form_class = PtoRequestForm
    success_url = '/accounts'
    # Pre-populates the form with the specified values on page load.
    def get_initial(self):
        return {'user': self.request.user}

    # Function runs when form is submitted. Do whatever needed to the form before it's saved to the db.
    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.user = self.request.user
        new_form.title = self.request.user.first_name
        new_form.save()
        return super(IndexView, self).form_valid(form)

    # Function runs on page load. Gather any information needed for the template.
    def get_context_data(self, **kwargs):
        # Initialize context
        context = super(IndexView, self).get_context_data(**kwargs)

        # Grab all ptoHistory records from the database, selecting only the values desired.
        pto_history = PtoHistory.objects.values('title', 'start', 'end', 'pk', 'user_id')
        # Convert the django queryset to json so that fullcalendar can work with it on the frontend.
        json_pto_history = json.dumps(list(pto_history), cls=DjangoJSONEncoder)
        # Save the converted json to the context to be returned to the front end.
        context['ptoHistory'] = json_pto_history
        return context


def login_view(request):
    title = "Login"
    user_form = UserLoginForm(request.POST or None)
    if user_form.is_valid():
        username = user_form.cleaned_data.get('username')
        password = user_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse('accounts:index', args=(username, )))
    return render(request, 'form.html', {'user_form':user_form, 'title':title})


def register_view(request):
    title = "Register"
    user_form = UserRegisterForm(request.POST or None)
    user_profile_form = UserProfileForm(request.POST or None)
    if user_form.is_valid() and user_profile_form.is_valid():
        user = user_form.save(commit=False)
        password = user_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        # Attach user profile to user account
        user.profile.pto_tier = request.POST.__getitem__('pto_tier')
        user.save()
        # Log in user
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/accounts/")

    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
        'title': title
    }
    return render(request, 'form.html', context)


def logout_view(request):
    logout(request)
    return redirect("/accounts/login/")
