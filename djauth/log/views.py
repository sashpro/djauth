from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib import auth


class LoginForm(FormView):
    form_class = AuthenticationForm
    template_name = "log/login.html"
    success_url = "/home"

    def form_valid(self, form):        
        self.user = form.get_user()
        auth.login(self.request, self.user)
        return super(LoginForm, self).form_valid(form)
        
        
class RegisterForm(FormView):
    form_class = RegForm
    success_url = "/"
    template_name = "log/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterForm, self).form_valid(form)

        
def home(request):
    if request.user.is_authenticated:
        return render(request, "log/home.html")
    else:
        return HttpResponseRedirect("/")     

    
def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
     
     
     
 