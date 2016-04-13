from django.shortcuts import HttpResponse, render
from django.template.context_processors import request
from imaplib import Response_code
from django.template import loader
from django.core.urlresolvers import reverse
#from polls.models import Question
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.regex_helper import Choice
from django.core.urlresolvers import reverse
from django.views import generic
from cgi import log
from re import template
from django.contrib.auth.models import User
# Create your views here.
"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    #try:
     #   question = Question.objects.get(pk = question_id)
    #except Question.DoesNotExist:
     #   raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""

class UserProfile(generic.ListView):
    model = User
    template_name = 'polls/profile.html'

class LoginView(generic.ListView):
    model = User
    template_name = 'polls/login.html'

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return 'thanh cong'

#def index(request):
 #   template = loader.get_template('polls/index.html')
  #  context = {'latest_question_list': 'thanh cong'}
   # return render(request, 'polls/index.html', context)

"""class DetailView(generic.DetailView):
    model = Question 
    template_name = 'polls/detail.html'
 
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
   """ 
    
def signup(request):
    return render(request, 'polls/signup.html')

"""def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print request.POST['choice']
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))"""