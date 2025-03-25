from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from full_videos.models import Following


def login_view(request):
    """Функція для обробки логіну користувача."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('videos-list')  # Вказати правильний маршрут (наприклад, 'videos-list')
            else:
                messages.error(request, 'Неправильне ім\'я користувача або пароль.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login_page.html', {'form': form})


def register_view(request):
    """Функція для обробки реєстрації нового користувача."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Збереження користувача
            login(request, user)  # Автоматичний вхід після реєстрації
            messages.success(request, 'Реєстрація успішна! Ви зараз увійшли.')
            return redirect('videos-list')  # Переконайтесь, що маршрут існує
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    """Функція для обробки виходу з облікового запису."""
    logout(request)
    messages.success(request, 'Ви успішно вийшли.')
    return redirect('accounts:login')  # Маршрут для логіну


def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        following_channels = Following.objects.filter(user=user)
        channels = [follow.channel for follow in following_channels]
        print(channels)

        return render(request, 'accounts/profile.html', {'user': user, 'following_channels': channels})