from django.urls import path

from contest.UIElements.pages.contests import listContests, editContest
from contest.UIElements.pages.problemDisplay import listProblems, viewProblem
from contest.views.contests import deleteContest, createContest
from contest.views.generic import login, root, logout
from contest.views.messages import getMessages


app_name = 'contest'
urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    # path('getMessages', getMessages, name='getMessages')

    # logged in required
    path('', root, name='root'),
    path('problems', listProblems, name='listProblems'),
    path('problems/<uuid:id>', viewProblem, name='viewProblem'),

    # admin
    path('contests', listContests, name='listContests'),
    path('contests/<uuid:id>', editContest, name='editContest'),
    # TODO: there are two 'editContest' funcs and no 'createContest funcs. ??
    path('editContest', createContest, name='saveNewContest'),
    path('contests/new', editContest, name='createNewContest'),
    path('deleteContest', deleteContest, name='deleteContest')
]
