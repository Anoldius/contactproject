from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def list_contacts(request):
    if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('#')
        
    
    all_my_contacts = Contact.objects.all().order_by('created_at')
    my_empyt_form = ContactForm()

    context = {
        'contacts_list': all_my_contacts,
        'form': my_empyt_form
    }

    return render(request, 'contacts/index.html', context)
