from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie_search/$', views.moviesearch, name='moviesearch'),
url(r'^load_data/$', views.loaddata, name='loaddata'),
url(r'^rate/$', views.rate, name='rate'),
url(r'^authenticate/$', views.authenticate, name='authenticate'),
url(r'^process/$', views.process, name='process'),
url(r'^newuser/$', views.newuser, name='newuser'),
url(r'^yesrateit/$', views.yesrateit, name='yesrateit'),
url(r'^myrating/$', views.myrating, name='myrating'),
url(r'^polo/$', views.polo, name='polo'),
url(r'^meet_the_team/$', views.meet_the_team, name='meet_the_team'),
url(r'^images/$', views.images, name='images'),
url(r'^clear/$', views.clear, name='clear'),
url(r'^searchmoviebyalphabet/$', views.searchmoviebyalphabet, name='searchmoviebyalphabet'),
url(r'^help/$', views.help, name='help'),
url(r'^ihaverated/$', views.ihaverated, name='ihaverated'),
]