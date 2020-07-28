from django.shortcuts import  get_object_or_404,render
from django.template import loader
# Create your views here.
from django.http import HttpResponse,  HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
#「载入模板，填充上下文，再返回由它生成的 HttpResponse 对象」
class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        "Return last five published questions"
        return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

#如果用戶知道連結訪問他們(在發布日期時未來的那些投票不會在目錄頁index裡出現)，卻還是可以訪問到他們
#在DetailView增加一些約束
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

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # 將命名url轉化為常規url
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # return HttpResponse("You're voting on question %s." % question_id)