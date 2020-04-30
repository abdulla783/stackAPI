from django.urls import path, include
from .views import index, QuestionAPI, questionSearch
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', QuestionAPI)

urlpatterns = [
    path('', index),
    path('questionsearch/', questionSearch, name='questionSearch'),
    path('', include(router.urls)),
]
