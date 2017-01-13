from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from accounts.views import (login_view, register_view, logout_view)
from . import views

app_name = 'accounts'

urlpatterns = [
    # root url will look like www.website.com/accounts/

    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^(?P<username>[0-9a-zA-Z._]+)/$', login_required(views.IndexView.as_view()), name = 'index'),

]
