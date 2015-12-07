import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from polls.models import Question, Choice
# Create your tests here.

class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose pub_date is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for questions whose pub_date is over a day in the past
		"""
		time = timezone.now() - datetime.timedelta(days=2)
		past_question = Question(pub_date=time)
		self.assertEqual(past_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() shoudl return True for questions whose pub_date is within a day old.
		"""
		time = timezone.now()
		current_question = Question(pub_date=time)
		self.assertEqual(current_question.was_published_recently(), True)

def create_question(question_text, days):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """