from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro
from django.views import View
from .forms import LibroForm

# Create your views here.

"""class LibroList(View):

    def get(self, request):
        libro = Libro.objects.all()
        return render(request, 'libros/libro_list.html', {'libro': libro})"""
    
class LibroList(ListView):
    
    model = Libro
    template_name = 'libros/libro_list.html'

    
"""class LibroDetalle(View):

    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'libros/libro_details.html', {'libro': libro})"""


class LibroDetalle(DetailView):

    model = Libro
    template_name = 'libros/libro_details.html'

    
class New(View):
          
    def get(self, request):
        form=LibroForm()
        return render(request, 'libros/new.html', {'form': form})
    
    def post(self, request):
        form=LibroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            autor = form.cleaned_data["autor"]
            rating = form.cleaned_data["rating"]
            sinopsis = form.cleaned_data["sinopsis"]

            Libro.objects.create(titulo = titulo, autor = autor, rating = rating, sinopsis = sinopsis)
            return redirect('libro_list')
        return render(request, 'libros/new.html', {'form': form})