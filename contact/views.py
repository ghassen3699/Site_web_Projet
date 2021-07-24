from django.shortcuts import render
from . import forms



def contact(request) :
    form = forms.ContactForm()
    if request.method == 'POST' :
        form = forms.ContactForm(request.POST)
        if form.is_valid() :
            form.save()
        else :
            return render(request,'contact/contact.html',{'form':form})
    return render(request,'contact/contact.html',{'form':form})




