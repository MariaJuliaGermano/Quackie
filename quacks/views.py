from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuackForm

@login_required
def quack_create(request):
    if request.method == 'POST':
        form = QuackForm(request.POST)

        if form.is_valid():
            quack = form.save(commit=False)
            quack.user = request.user
            quack.save()
            return redirect('home')
    else:
        form = QuackForm
    return render(request, 'quacks/quack_create.html', {'form': form})