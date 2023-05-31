from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .forms import UsernameChangeForm


def signup(request):  # 회원 가입
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def login(request):    # 로그인
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')


@login_required
def logout(request):    # 로그아웃
    auth_logout(request)
    return redirect('index')


@login_required
def profile(request):   # 프로필
    return render(request, 'users/profile.html')


@login_required
def user_update(request):   # 회원 정보 수정
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UsernameChangeForm(instance=request.user)
    return render(request, 'users/update_profile.html', {'form': form})


@login_required
def user_delete(request):   # 회원 탈퇴
    if request.method == 'POST':
        request.user.delete()
        return redirect('index')
    return render(request, 'users/delete_account.html')
