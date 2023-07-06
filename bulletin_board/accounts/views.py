from allauth.account.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from .forms import UserCodeForm, SignUpForm, LogInForm
from .models import UserCode


class ConfirmCode(FormView):
    model = UserCode
    form_class = UserCodeForm
    template_name = 'registration/confirm_code.html'
    success_url = reverse_lazy('login')
    context_object_name = 'confirm_code'

    def form_valid(self, form):
        code_use = form.cleaned_data['code']
        if UserCode.objects.filter(code=code_use):
            user_code = UserCode.objects.get(code=code_use)
            user_code.user.is_active = True
            user_code.user.save()
            return super().form_valid(form)
        else:
            message = 'Confirmation code is incorrect'
            return HttpResponse(message)


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('confirm_code')
    template_name = 'registration/signup.html'


class LogIn(LoginView):
    form_class = LogInForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        redirect('anno_list')
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('login')
