from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns=patterns('',
                     url(r'^signup/',TemplateView.as_view(template_name="signup.html")),
                     url(r'^signedin/','gtracker.views.signup',name='signedup'),
                     url(r'^login/',TemplateView.as_view(template_name="login.html")),
                     url(r'^loggedin/','gtracker.views.login',name='loggedin'),
                     url(r'^addg/',TemplateView.as_view(template_name="addg.html")),
                     url(r'^userdata/','gtracker.views.addg', name='userdata'),
                     url(r'^userowndata/','gtracker.views.addgown', name='userowndata'),
                     url(r'^details/(?P<b3>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', 'gtracker.views.details' , name='details'),)

