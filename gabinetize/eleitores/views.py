from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Eleitor
from .forms import EleitorForm

def adicionar_eleitor(request):
    if request.method == 'POST':
        form = EleitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eleitores')
    else:
        form = EleitorForm()
    return render(request, 'eleitores/adicionar_eleitor.html', {'form': form})

def editar_eleitor(request, pk):
    eleitor = get_object_or_404(Eleitor, pk=pk)
    if request.method == 'POST':
        form = EleitorForm(request.POST, instance=eleitor)
        if form.is_valid():
            form.save()
            return redirect('lista_eleitores')
    else:
        form = EleitorForm(instance=eleitor)
    return render(request, 'eleitores/editar_eleitor.html', {'form': form})

def excluir_eleitor(request, pk):
    eleitor = get_object_or_404(Eleitor, pk=pk)
    if request.method == 'POST':
        eleitor.delete()
        return redirect('lista_eleitores')
    return render(request, 'eleitores/excluir_eleitor.html', {'eleitor': eleitor})

def lista_eleitores(request):
    eleitores = Eleitor.objects.all()
    return render(request, 'eleitores/lista_eleitores.html', {'eleitores': eleitores})

