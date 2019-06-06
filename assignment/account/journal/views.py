from django.shortcuts import render, redirect
from .forms import journalForm

# Create your views here.
def journal(request):
    return render(request,'journal/index.html')

def add(request):
    if request.method == "POST":
        form = journalForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('journal/index.html')
            except:
                pass
    else:
        form=journalForm()
    return render(request,'journal/add.html',{'form':form})
def show(request):
    journal=journal.objects.get(id=id)
    return render(request,"index.html",{'journal':journal})
def edit(request,id):
    journal=journal.objects.get(id=id)
    return render(request,'journal/edit.html',{'journal':journal})
def update(request,id):
    j=journal.objects.get(id=id)
    form=journalForm(request.POST,instance=journal)
    if form.is_valid():
        form.save()
        return redirect('journal/index.html')
    return render(request,'journal/edit.html',{'journal':journal})
def destroy(request,id):
    journal=journal.objects.get(id=id)
    journal.delete()
    return redirect('journal/index.html')