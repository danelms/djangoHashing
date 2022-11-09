from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib

def home(request):
    #if the request is of type 'POST' check we have the hash of form input
    if request.method == 'POST':
        print(request.POST)
        filledForm = HashForm(request.POST)
        if filledForm.is_valid():
            #get text from text field
            clearText = filledForm.cleaned_data['text']
            #hash it
            hashText = hashlib.sha256(clearText.encode('utf-8')).hexdigest()
            #see if the Hash is already in the database
            try:
                hashPulled = Hash.objects.get(hash=hashText)
            except Hash.DoesNotExist:
                #if not, save it to the database
                newHash = Hash()
                newHash.text = clearText
                newHash.hash = hashText
                newHash.save()
            return redirect('hash', hash=hashText)


    form = HashForm()
    return render(request, 'hashing_app/home.html', {'form': form})

def hash(request, hash):
    #get Hash from db
    hashObj = Hash.objects.get(hash=hash)
    #pass Hash to hashing/whatever.html
    return render(request, 'hashing_app/hash.html', {{'hash':hashObj}})
