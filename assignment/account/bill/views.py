from django.shortcuts import render

# Create your views here.
def bill(request):
	return render(request,'bill/index.html')