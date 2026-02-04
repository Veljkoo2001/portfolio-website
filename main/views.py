from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def home_view(request):
    return render(request, 'main/home.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Dobij podatke iz forme
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Kreiraj subject i body za email
            subject = f"Nova poruka od {name} sa portfolia"
            body = f"""
            Ime: {name}
            Email: {email}
            
            Poruka:
            {message}
            """
            
            # Pošalji email (u produkciji koristi SMTP settings)
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],  # Pošalji sebi
                    fail_silently=False,
                )
                messages.success(request, 'Poruka je uspešno poslata! Odgovoriću u najkraćem roku.')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'Došlo je do greške prilikom slanja: {e}')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})