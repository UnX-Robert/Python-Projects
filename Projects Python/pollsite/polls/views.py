from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question



# Create your views here.
class IndexView(generic.ListView):
	
	template_name = "polls/index.html"
	context_object_name = "latest_question_list"

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(response, question_id):
	q = get_object_or_404(Question, pk=question_id)

	try:
		selected_choice = q.choice_set.get(pk=response.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
	    # Redisplay the question voting form.
		return render(response, 'polls/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))