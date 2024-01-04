from typing import Any
from django.db import models
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# Create your views here.
# def index(request):
#     latest_question_list=Question.objects.order_by("-pub_date")[:5]
#     # template=loader.get_template("myapp/index.html")
#     # output=",".join([q.question_text for q in latest_question_list])
#     context={"latest_question_list":latest_question_list}
#     # return HttpResponse(template.render(context,request))
#     return render(request,"myapp/index.html",context)

# def detail(request, question_id):
#     # try:
#     #     question=Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question not found")

#     # # return HttpResponse("You're looking at question %s." % question_id)
#     # return render(request,'myapp/detail.html',{"question":question})
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "myapp/detail.html", {"question": question})


# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,"myapp/results.html",{"question":question})


class IndexView(generic.ListView):
    template_name="myapp/index.html"
    context_object_name="latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]    
    
class DetailView(generic.DetailView):
    model=Question
    template_name="myapp/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model=Question
    template_name="myapp/results.html"

def vote(request, question_id):

    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,"myapp/detail.html",{"question":question,"error_message":"you didnt select a choice"})
   
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("myapp:results", args=(question.id,)))