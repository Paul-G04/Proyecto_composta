from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import RegisterForm
from .models import Article


def home(request):

    articles = Article.objects.filter(
        published=True
    ).prefetch_related(
        'categories'
    ).select_related('owner')

    return render(request, 'compostas/home.html', {
        'articles': articles
    })


def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Tu cuenta fue creada correctamente.'
            )

            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'compostas/register.html', {
        'form': form
    })


def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                'Bienvenido a PAEC Compostas.'
            )

            return redirect('home')

        messages.error(
            request,
            'Usuario o contraseña incorrectos.'
        )

    return render(request, 'compostas/login.html')


@require_POST
def logout_view(request):

    logout(request)

    messages.success(
        request,
        'Sesión cerrada correctamente.'
    )

    return redirect('home')