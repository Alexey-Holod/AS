from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import AuthRegUserForm
from django.contrib.auth.models import User
from .models import Profile

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
            # UserPhone = User.objects.get(id=request.user)
            first_name = form.cleaned_data.get('first_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, first_name=first_name, password=password)
            login(request, user)

            # -----------------------------------------

            UserPhone = Profile.objects.get(user = request.user.id)
            UserPhone.Phone = form.cleaned_data.get('phone')
            UserPhone.save()
            print('ХУЙЙЙЙЙ', UserPhone.Phone)

            # -----------------------------------------

            return redirect('/')
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
