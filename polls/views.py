from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,Http404
from django.urls import reverse
from django.views import generic
import json

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        data = super(ResultsView,self).get_context_data(**kwargs)
        id_ = data['question'].id
        q = Question.objects.get(pk = id_)
        evaluated_chocies = []
        qs = q.get_choices()
        for item in qs:
            evaluated_chocies.append(item.votes)
        data['choices'] = evaluated_chocies
        return data


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {'question' : question, 'error_message':"You didn't select a choice"})
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
