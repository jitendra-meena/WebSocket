from django.shortcuts import render
from django.views import View
from .models import ChatModel
from django.contrib.auth.models import User

class Whatsapp(View):
    def get(self,request):
        users = User.objects.exclude(username = request.user.username,is_superuser=False)
        print("Users",users)
        return render(request,'index.html',context={'users': users})

        
    

class Chat(View):
    def get(self,request,username):
        user_obj = User.objects.get(username=username)
        users = User.objects.exclude(username=request.user.username,is_superuser=False)
        print("User",users,user_obj)

        if request.user.id > user_obj.id:
            print("Yes")
            thread_name = f'chat_{request.user.id}-{user_obj.id}'
            print("thread_name",thread_name)
        else:
            thread_name = f'chat_{user_obj.id}-{request.user.id}'
            print("No")
        message_objs = ChatModel.objects.filter(thread_name=thread_name)
        return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})


