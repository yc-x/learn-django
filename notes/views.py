from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Notes


# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"   # here defines the name of context dicitonary
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
    
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk = pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})