from django.shortcuts import redirect, render

from .forms import AlunoForm
from .models import Aluno


def criar_aluno(request):
    if request.method == "GET":
        form = AlunoForm()
    elif request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
            return redirect("listar_aluno")
    return render(request, "form.html", {"form": form})


def listar_aluno(request):
    alunos = Aluno.objects.all()
    context = {"alunos": alunos}

    return render(request, "index.html", context)
