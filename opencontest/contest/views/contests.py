import json

from django.http import JsonResponse

from contest import register
from contest.auth import admin_required
from contest.models.contest import Contest
from contest.models.problem import Problem


@admin_required
def deleteContest(request, *args, **kwargs):
    id = request.POST['id']
    Contest.get(id).delete()
    return JsonResponse("ok", safe=False)


@admin_required
def createContest(request):
    """POSTing a freshly-created contest redirects here courtesy of script.js."""
    if request.method == 'POST':
        id = request.POST.get("id")
        contest = Contest.get(id) or Contest()

        contest.name = request.POST.get("name")
        contest.start = int(request.POST.get("start"))
        contest.end = int(request.POST.get("end"))
        contest.scoreboardOff = int(request.POST.get("scoreboardOff"))
        contest.problems = [Problem.get(id) for id in json.loads(request.POST.get("problems"))]

        contest.save()

        # return contest.id
        return JsonResponse(contest.id, safe=False)
    else:
        pass


# TODO: move to urls
# register.post("/deleteContest", "admin", deleteContest)
# register.post("/editContest", "admin", editContest)
