from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.team, name='roster_home'),
    url(r'^player/$', views.playerList, name='roster_player_list'),
    url(r'^player/(?P<pk>\d+)$', views.player, name='roster_player'),
    url(r'^coach/(?P<pk>\d+)$', views.coach, name='roster_coach'),
    )