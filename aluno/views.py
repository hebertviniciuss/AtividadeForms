from django.shortcuts import render
from .forms import MatriculaForm
# Create your views here.
def criar_matricula(request):
    
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            form = MatriculaForm()
    else:
        form = MatriculaForm()
    
    return render(request,"aluno/form.html", {'form':form})