import json

from django.http import JsonResponse

from contest import register
from contest.models.problem import Datum, Problem


def deleteProblem(params, setHeader, user):
    id = params["id"]
    Problem.get(id).delete()
    return "ok"


def createProblem(request):
    id = request.POST.get("id")
    problem = Problem.get(id) or Problem()

    problem.title = request.POST["title"]
    problem.description = request.POST["description"]
    problem.statement = request.POST["statement"]
    problem.input = request.POST["input"]
    problem.output = request.POST["output"]
    problem.constraints = request.POST["constraints"]
    problem.samples = int(request.POST["samples"])

    testData = json.loads(request.POST["testData"])
    problem.testData = [Datum(d["input"], d["output"]) for d in testData]
    problem.tests = len(testData)

    problem.save()

    return JsonResponse(problem.id, safe=False)


# TODO: move to urls
# register.post("/deleteProblem", "admin", deleteProblem)
# register.post("/editProblem", "admin", editProblem)
