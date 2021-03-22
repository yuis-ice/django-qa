
# from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from qaapp.forms import tmpForm
from qaapp.forms import AnswerForm
from django.contrib import messages
import json

from django.contrib.auth.models import User
from qaapp.models import Question, Answer
from django.http import HttpResponse, HttpResponseRedirect

import datetime
import textwrap

from django.conf import settings
# from django.conf import settings as conf_settings
from django.contrib.auth.decorators import login_required

from django.core.serializers.json import DjangoJSONEncoder

from django.urls import reverse

# Create your views here.


def dev(request):

    jsonobj = json.dumps(
        {
            # "request.user": request.user,
            "request.user.email": request.user.email if request.user.is_authenticated else "",
            "request.user.is_authenticated": request.user.is_authenticated,
            "user.is_anonymous": request.user.is_anonymous ,
            "user.is_active": request.user.is_active ,
            "user.is_superuser": request.user.is_superuser ,
            "user.is_staff": request.user.is_staff ,
            # user.last_login
            'user_permissions_': list(request.user.user_permissions.values()),
            'config': list(request.user.config.values()) if hasattr(request.user, "config") else "" ,
            # 'groups_': list(request.user.groups.filter(name = "level0").values()),
            'groups_': list(request.user.groups.values()),
        },
        sort_keys=True, 
        indent=4,
        cls=DjangoJSONEncoder,
    )
    print(jsonobj)
    return HttpResponse( jsonobj, content_type="application/json" ) 




@login_required(login_url=settings.LOGIN_URL)
# def tmp(request):
def tmp(request):

    content_default = textwrap.dedent(
        '''What is your question? 
        '''
    )
    
    # if 'delete' in self.data:
    # if 'delete' in request.POST:
    #     if Question.objects.filter(user=request.user).exists():
    #         Question.objects.filter(user=request.user).first().delete()
    #         messages.success(request, "Deleted.")
    #     else:
    #         messages.error(request, "No config file exists.")
            
    #     # return render(request, 'qaapp/tmp.html', {'form': f})
    #     return render(request, 'qaapp/tmp.html', { 'form': tmpForm(initial={'content': content_default}) })

    if request.method == 'POST':
        # f = UserCreationForm(request.POST)
        f = tmpForm(request.POST)
        # f = tmpForm(request.POST, initial={'json': '{hogehoge}'})
        if f.is_valid():
            # messages.success(request, 'form valid.')

            # try:
            #     # json_object = json.loads(myjson)
            #     obj = json.loads(f.data["json"])
            # except ValueError as e:
            #     # return False
            #     messages.error(request, e) # invalid JSON
            #     # return redirect('./')
            #     return render(request, 'qaapp/tmp.html', {'form': f})
            # # return True

            messages.success(request, 'content successfully updated.')

            print(f.data["content"])

            # request.user
            # user.config.get_or_create(json="hoge")
            # f.save()
            # Question.objects.get_or_create(json=f.data["json"])
            # Question.objects.get_or_create(user=request.user.id, json=f.data["json"])
            # Question.objects.get_or_create(user=request.user, json=f.data["json"])

            # if Question.objects.filter(user=request.user).exists():
            #     config = Question.objects.filter(user=request.user).first()
            #     config.content = f.data["content"]
            #     config.save()
            # else:
            #     Question.objects.get_or_create(user=request.user, content=f.data["content"])
            
            question = Question.objects.get_or_create(user=request.user, content=f.data["content"])
            question_id = question[0].id

            # return redirect('register')
            # return redirect('tmp')
            # return redirect('tmpview')
            # return redirect('qaapp/tmp.html')
            # return redirect('./') # this resets the form, and shows the initial json
            
            # return redirect('devview')
            print(
                # reverse('devview'),  
                # reverse('qaapp:devview'),
                # reverse('question'),
                # reverse('question', kwargs={'question_id': 3}),
                reverse('question', kwargs={'question_id': question_id}),
                # request.build_absolute_uri()
            )
            # return redirect(reverse('qaapp:devview'))
            # return redirect(reverse('qaapp:devview', kwargs={'hoge': hoge}))
            return redirect(reverse('question', kwargs={'question_id': question_id}))
            
            # return render(request, 'qaapp/tmp.html', {'form': f}) # this preserves the form 

    else:
        # f = UserCreationForm()
        # f = tmpForm()
        # f = tmpForm(initial={'json': '{hogehoge}'})
        # if Question.objects.filter(user=request.user).exists():
        #     jsonstring = Question.objects.filter(user=request.user).first().json
        #     f = tmpForm(initial={'json': jsonstring})
        # else:
        #     f = tmpForm(initial={'json': jsonstring_defaultconfig})

        # f = tmpForm(auto_id=False)
        
        f = tmpForm(initial={'content': content_default})

    # return render(request, 'users/register.html', {'form': f})
    return render(request, 'qaapp/tmp.html', {'form': f})
    # return HttpResponse("Hello, world. You're at the users index.")


# def index(request):
    # return render(request, "index.html", context={})
    # return 0

@login_required(login_url=settings.LOGIN_URL)
# def edit(request):
def edit(request, question_id):

    # template_name = 'qaapp/question_edit.html'
    # model = Question
    # context_object_name = 'question' 

    question = Question.objects.get_or_create(id=question_id)

    if 'delete' in request.POST:
        question[0].delete()
        messages.success(request, "Deleted.")
        # return redirect(reverse('home'))
        return redirect(reverse('index'))
    

    if request.method == 'POST':
        f = tmpForm(request.POST)

        if f.is_valid():            
            # print(f.data["content"])
            
            question = Question.objects.update_or_create(id=question_id)
            question[0].content = f.data["content"]
            question[0].save()

            messages.success(request, 'content successfully updated.')
            return redirect("./")

    else:        
        # question = Question.objects.get_or_create(id=question_id)
        print(
            # request.GET.keys(), 
            # question_id
            # question[0].id , 
            # question[0].content
        )
        f = tmpForm(initial={'content': question[0].content})

    # return render(request, 'qaapp/tmp.html', {'form': f})
    # return render(request, 'qaapp/tmp.html', {'form': f, 'question': question})
    return render(request, 'qaapp/question_edit.html', {'form': f, 'question': question})

    # return HttpResponse( "hoge.", content_type="application/json" ) 


@login_required(login_url=settings.LOGIN_URL)
def answer_new(request, question_id):
    
    if request.method == 'POST':
        f = AnswerForm(request.POST)

        if f.is_valid():

            # question = Question.objects.get_or_create(user=request.user, content=f.data["content"])
            answer = Answer.objects.update_or_create(user=request.user, question_id=question_id, content=f.data["content"])
            answer_id = answer[0].id
            
            messages.success(request, 'content successfully updated.')
            # print(f.data["content"])

            return redirect(reverse('question', kwargs={'question_id': question_id}))

    else:
        f = AnswerForm(initial={'content': "What is your answer?"})

    return render(request, 'qaapp/answer_new.html', {'form': f})



@login_required(login_url=settings.LOGIN_URL)
def answer_edit(request, answer_id):

    answer = Answer.objects.get_or_create(id=answer_id)
    question_id = Answer.objects.filter(id=answer_id)[0].question_id

    # print(
    #     "answer_id ..",
    #     answer_id, 
    #     answer,
    #     question_id
    # )
    
    if 'delete' in request.POST:
        answer[0].delete()
        messages.success(request, "Deleted.")
        # return redirect(reverse('home'))
        # return redirect(reverse('index'))
        # return redirect("./")
        return redirect(reverse('question', kwargs={'question_id': question_id}))
    

    if request.method == 'POST':
        f = AnswerForm(request.POST)

        if f.is_valid():            
            # print(f.data["content"])
            
            answer = Answer.objects.update_or_create(id=answer_id)
            answer[0].content = f.data["content"]
            answer[0].save()

            messages.success(request, 'content successfully updated.')
            return redirect("./")

    else:        
        f = AnswerForm(initial={'content': answer[0].content})

    # return render(request, 'qaapp/answer_edit.html', {'form': f, 'answer': answer})
    return render(request, 'qaapp/answer_edit.html', {'form': f, 'answer': answer, 'question_id': question_id})