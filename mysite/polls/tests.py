
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time=timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_questions = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time=timezone.now() - datetime.timedelta(hours=23, minutes=69, seconds=59)
        recent_question=Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)

    def create_question(question_text, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return

    Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response=self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertComtains(response, "No polls are available.")
        self.assetQuerysetEqual(response.content['latest_question_list'],[])

    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.content['latest_question_list'],['<Question: Past question.>'])

    def test_future_question(self):
        create_questions(question_text="Future question.", days=30)
        response=self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQueryEqual(response.context['latest_question_list'],[])

    def test_future_question_and_past_question(self):
        create_question(question_text="Past question.",days=-30)
        create_question(question_text="Future question.", days=30)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_quesion_list'],['<Question:Past question.>'])


    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Pats question 2.", days=-5)
        self.assertQuerysetEqual(ersponse)

