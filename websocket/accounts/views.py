from email import message
from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User


class Register(View):
    def get(self,request):
        form = SignUpForm()
        return render(request,'accounts/register.html')
    
    def post(self,request):
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        cnf_password = request.POST.get('password2')
        
        if not User.objects.filter(username = username,is_active = True).exists():
            if password==cnf_password:
                user = User(username =username,first_name=name,email=email,password=password)
                user.save()
                user.set_password(password)
                user.save()
                return redirect('/')
            else:
                messages.error(request, "Password Not Match !")
                return render(request,'accounts/register.html')
        else:
            messages.error(request, "user Already Exits")
            return render(request,'accounts/register.html')
    
        



class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/core/whatsapp/')
        return render(request,'accounts/login.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                # messages.success(request, "Login successful." )
                return redirect('/core/whatsapp/')
            else:
                messages.error(request, "Account Not Active")
                return render(request,'accounts/login.html')
        else:
            messages.error(request, f"NO ACCOUNT FOUND WITH USERNAME {username} AND PASSWORD {password}")
            return render(request,'accounts/login.html')    
                
            
    










# # Create your views here.

# User = get_user_model()


# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)

#         if form.is_valid():
#             new_user = form.save()
#             new_user = authenticate(username=form.cleaned_data['username'],
#                                     password=form.cleaned_data['password1'],
#                                     )
#             login(request, new_user)

#             return HttpResponseRedirect(reverse('home'))

#     else:
#         form = SignUpForm()

#     return render(request, 'accounts/register.html', {'form': form})


# def loginView(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('home'))

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 return HttpResponse("Account Not Active")
#         else:
#             context = {'notfound': True}
#             print(
#                 f"NO ACCOUNT FOUND WITH USERNAME {username} AND PASSWORD {password}")
#             print(context)
#             return render(request, 'accounts/login.html', context)

#     else:
#         return render(request, 'accounts/login.html')