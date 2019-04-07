from django.urls import path

from contest.views.generic import login

app_name = 'contest'
urlpatterns = [
    path('login', login, name='login')
]
