from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Aluno

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlunoForm()
    return render(request, 'cadastrar.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'editar.html', {'form': form, 'aluno': aluno})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('home')

def detalhar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'detalhe.html', {'aluno': aluno})