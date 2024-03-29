from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'firstApp/index.html', context)

def details(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExits:
        raise Http404('question doesnot exit')
    return render(request,'firstApp/details.html',{'question':question})

def results(request,question_id):
    response = "you're looking at the results of question %s"
    return HttpResponse(response %question_id)

def vote(request,question_id):
    response = "you are looking at the result of questoin %s"
    return HttpResponse(response %question_id)
