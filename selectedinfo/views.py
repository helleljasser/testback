# selectedinfo/views.py
from django.shortcuts import render, redirect
from .models import SelectedText

def save_selected_text(request):
    if request.method == 'POST':
        selected_text = request.POST.get('selected_text', '')
        SelectedText.objects.create(text=selected_text)
        return redirect('success_page')  # Redirige vers une page de succès ou autre

    return render(request, 'selectedinfo/form.html')  # Affiche un formulaire pour le texte sélectionné
