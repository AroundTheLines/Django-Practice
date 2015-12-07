from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		"""
		Returns if whether the question was published within the past day. Pinned down with tests.
		"""
		now = timezone.now()
		# If the current time - 1 day is less than the publishing date (checks if made within day) AND 
		# the publishing date is earlier current date, return true (checks for future)
		return now - datetime.timedelta(days=1) <= self.pub_date <= now


@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text