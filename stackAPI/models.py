from django.db import models

# Create your models here.
class Question(models.Model):
    question_title = models.CharField(max_length=300)
    question_tag = models.CharField(max_length=250)
    question_url = models.URLField(max_length=300)
    question_view_count = models.CharField(max_length=50, null=True, blank=True)
    question_answer_count = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.question_title
    