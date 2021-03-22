from django.views.generic import TemplateView

from django.views.generic import DetailView
from django.views.generic import ListView

from qaapp.models import Question, Answer
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from django.views.generic import View, FormView
from qaapp.forms import tmpForm
from django.shortcuts import render, redirect

# class IndexPageView(TemplateView):
#     template_name = 'main/index.html'



class QuestionList(ListView):

    # question_list.html
    model = Question
    context_object_name = 'questions' # also "object_list"

    def get_context_data(self, **kwargs):
        # context = super(AboutView, self).get_context_data(**kwargs)
        # context['dahl_books'] = Books.objects.filter(author="Dahl')
        # data['hoge'] = "hogehoge"
        context = super().get_context_data(**kwargs)
        context['hoges'] = "hogehoge"
        # context['myquestions'] = Question.objects.filter(user=request.user)
        
        # context['myquestions'] = Question.objects.filter(user=self.request.user)
        if self.request.user.is_authenticated:
            context['myquestions'] = Question.objects.filter(user=self.request.user)
        
        return context

# class PublisherBookList(ListView):
class UserQuestionList(ListView):

    template_name = 'qaapp/questions_by_user.html'

    def get_queryset(self):
        # self.user = get_object_or_404(User, name=self.kwargs['user'])
        self.user_id = get_object_or_404(User, id=self.kwargs['user_id'])
        # return Book.objects.filter(publisher=self.publisher)
        # print(
        #     Question.objects.filter(user_id=self.user_id)
        # )
        return Question.objects.filter(user_id=self.user_id)

# class QuestionView(TemplateView): 
class QuestionView(ListView): 
    
    template_name = 'qaapp/question.html'
    model = Question
    context_object_name = 'question' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['hoges'] = "hogehoge"
        # context['myquestions'] = Question.objects.filter(user=self.request.user)
        # Answer.objects.update_or_create(user_id=1, question_id=1, content="cat is an animal. Period.")
        # Answer.objects.filter(question_id=1)
        context['answers'] = Answer.objects.filter(question_id=self.kwargs['question_id'])
        return context

    def get_queryset(self):
        # self.user = get_object_or_404(User, name=self.kwargs['user'])
        # self.question = get_object_or_404(Question, id=self.kwargs['question_id'])

        # return Book.objects.filter(publisher=self.publisher)
        # print(
        #     Question.objects.filter(user_id=self.user_id)
        # )
        print(
            # "hogehoge", 
            # Question.objects.filter(id=self.kwargs['question_id'])
            # self.question, 
        )
        return Question.objects.filter(id=self.kwargs['question_id'])
        # return Question.objects.filter(id=self.question)

# class QuestionEditView(ListView): 
# class QuestionEditView(FormView): 


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


class MetaView(TemplateView):
    template_name = 'main/meta.html'
