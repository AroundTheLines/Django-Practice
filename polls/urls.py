from django.conf.urls import url

from . import views

# app_name to define subpages for django in case of multiple apps
#app_name = 'polls'
#urlpatterns = [
#	url(r'^$', views.index, name='index'),
#	# Polls/question_id
#	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
#	# Polls/question_id/results
#	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
#	# Polls/question_id/vote
#	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#]

# Note that the app_name line has shifted from polls.urls to mysite.urls.
# That occurs with generic views!
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]