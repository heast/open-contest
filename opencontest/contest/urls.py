from django.urls import path

from contest.UIElements.pages.contests import listContests, editContest
from contest.UIElements.pages.problemDisplay import listProblems, viewProblem
from contest.UIElements.pages.problemEdit import editProblem, newProblem, listProblemsAdmin
from contest.UIElements.pages.static import setup
from contest.views.contests import deleteContest, createContest
from contest.views.generic import login, root, logout
from contest.views.messages import getMessages
from contest.views.problems import deleteProblem, createProblem

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
    path('contests/<uuid:id>', editContest, name='editContestAdmin'),
    path('editContest', createContest, name='saveNewContest'),
    path('contests/new', editContest, name='createNewContest'),
    path('deleteContest', deleteContest, name='deleteContest'),

    path('problems_mgmt', listProblemsAdmin, name='adminListProblems'),
    path('problems/new', newProblem, name='newProblem'),
    path('problems/<uuid:id>/edit', editProblem, name='editProblem'),
    path('editProblem', createProblem, name='anotherEditProblem'),
    path('deleteProblem', deleteProblem, name='deleteProblem'),

    path('setup', setup, name='setup')

]
