from django.shortcuts import render

# Create your views here.
def ladger(request):
	return render(request,'ladger/index.html')