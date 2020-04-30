from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .seralizers import QuestionSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import pprint

# Create your views here.
def index(request):
    return HttpResponse("Working")

class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def questionSearch(request):
    if request.method == 'GET':
        question_title = request.GET.get('title',)
        question_tag = request.GET.get('tag',)
        url = 'https://api.stackexchange.com/' + f'2.2/search/advanced?order=desc&sort=activity&q={question_title}&accepted=False&answers=1&tagged={question_tag}&site=stackoverflow'
        resp = requests.get(url)
        resp = resp.json()
        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(resp)
        questions = []
        question_data = {}
        new_question = Question()
        for i in resp["items"]:
            if i["is_answered"]:
                new_question.question_title = i["title"]
                new_question.question_tag = i["tags"]
                new_question.question_url = i["link"]
                new_question.question_view_count = i["view_count"]
                new_question.answer_count = i["answer_count"]
                question_data = {
                'question_url': i["link"],
                'question_title': i["title"],
                'question_tag': i["tags"],
                'question_view_count': i["view_count"],
                'question_answer_count': i["answer_count"]
                }
            new_question.save() 
            questions.append(question_data)



        # for i in resp["items"]:
        #     if i["is_answered"]:
        #         question_data = {
        #         'question_url': i["link"],
        #         'question_title': i["title"],
        #         'question_tag': i["tags"],
        #         'question_view_count': i["view_count"],
        #         'question_answer_count': i["answer_count"]
        #         }
        #     questions.append(question_data)
        # total = []
        # for item in questions:
        #     for key in item.keys():
        #         total.append(item[key])
        #         question = Question()
        #         for i in total:
        #             question.question_url = i
        #             question.question_title = i
        #             question.question_tag = i
        #             question.question_view_count = i
        #             question.question_answer_count = i  
        #         question.save()

    paginator = Paginator(questions, 9)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(questions, index=4)
    
    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'questions': questions,
        'page_range': page_range
    }

    return render(request, 'stackAPI/index.html', context)

def proper_pagination(questions, index):
    start_index = 0
    end_index = 7
    if questions.number > index:
        start_index = questions.number - index # 1
        end_index = start_index + end_index # 1+7 = 8 
    return (start_index, end_index)