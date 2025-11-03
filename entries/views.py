from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Entry
from .forms import EntryForm

# Create your views here.
def dashboard(request):
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'entries/dashboard.html', {'entries': entries})

def entry_new(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New entry created successfully!')
            return redirect('dashboard')
    else:
        form = EntryForm()
    return render(request, 'entries/form.html', {'form': form})

