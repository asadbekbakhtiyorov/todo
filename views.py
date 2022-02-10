from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from .models import Todo


def all_todos(request):
    if request.user.is_authenticated:
        todo_list = Todo.objects.filter(user=request.user)
        return render(request, 'ToDo.html', {'todo_list':todo_list})
    else:
        return redirect('login')


def remove(request,son):
    if request.user.is_authenticated:
        del_to = Todo.objects.get(id = son)
        del_to.delete()
        return redirect('todo')
    else:
        return redirect('todo')


def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            Todo.objects.create(
                title=request.POST['t'],
                details =request.POST['d'],
                status=request.POST['s'],
                user=request.user
            )
            return redirect('todo')
    else:
        return redirect('login')


def loginView(request):
    if request.method=='POST':
        l = request.POST['login']
        parol = request.POST['parol']
        user = authenticate(request, username=l, password=parol)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('todo')
    return render(request, 'ToDo.html')


def registration(request):
    if request.method=='POST':
        user = User.objects.create_user(
            username = request.POST['login'],
            password = request.POST.get('parol')
        )
        login(request,user)
        return redirect('todo')
    return render(request, 'ToDo.html')


def LogoutView(request):
    logout(request)
    return redirect('login')