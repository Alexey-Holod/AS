from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import AuthRegUserForm

class Reg(View):
    template_name = 'auth_user_do/reg.html'

    def get(self, request):
        context = {
            'form': AuthRegUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthRegUserForm(request.POST)

        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, first_name=first_name, password=password)
            login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
