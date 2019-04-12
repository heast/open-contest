import markdown2
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

from contest import register
from contest.UIElements.lib.htmllib import UIElement, div, h2, h, h1
from contest.UIElements.lib.page import Card, Page
from contest.auth import logged_in_required
from contest.models.problem import Problem
from contest.models.contest import Contest
from contest.models.user import User


def formatMD(md: str) -> str:
    """ Convert Markdown to HTML """
    return markdown2.markdown(md, extras=["tables"])


class CodeEditor(UIElement):
    def __init__(self):
        self.html = div(cls="code-editor card", contents=[
            div(cls="card-header", contents=[
                h2("Code Editor", cls="card-title"),
                h.select(cls="language-picker custom-select col-2 custom-select-sm")
            ]),
            div(cls="ace-editor-wrapper", contents=[
                div(id="ace-editor", cls="ace-editor", contents=[
                    "#Some Python code"
                ])
            ])
        ])


def getSample(datum, num: int) -> Card:
    return Card("Sample #{}".format(num), div(cls="row", contents=[
        div(cls="col-6", contents=[
            h.p("Input:", cls="no-margin"),
            h.code(datum.input.replace("\n", "<br/>").replace(" ", "&nbsp;"))
        ]),
        div(cls="col-6", contents=[
            h.p("Output:", cls="no-margin"),
            h.code(datum.output.replace("\n", "<br/>").replace(" ", "&nbsp;"))
        ])
    ]))


@logged_in_required
def viewProblem(request, *args, **kwargs):
    # problem = Problem.get(params[0])
    problem = Problem.get(kwargs.get('id'))
    user = User.get(request.COOKIES.get('user'))

    if not problem:
        return JsonResponse(data='', safe=False)

    if not user.isAdmin():
        # Hide the problems till the contest begins for non-admin users
        if not Contest.getCurrent():
            return JsonResponse(data='', safe=False)
        if problem not in Contest.getCurrent().problems:
            return JsonResponse(data='', safe=False)

    return HttpResponse(Page(
        h.input(type="hidden", id="problem-id", value=problem.id),
        h2(problem.title, cls="page-title"),
        div(cls="problem-description", contents=[
            Card("Problem Statement", formatMD(problem.statement), cls="stmt"),
            Card("Input Format", formatMD(problem.input), cls="inp"),
            Card("Output Format", formatMD(problem.output), cls="outp"),
            Card("Constraints", formatMD(problem.constraints), cls="constraints"),
            div(cls="samples",
                contents=list(map(lambda x: getSample(x[0], x[1]), zip(problem.sampleData, range(problem.samples)))))
        ]),
        CodeEditor(),
        div(cls="align-right", contents=[
            h.button("Test Code", cls="button test-samples button-white"),
            h.button("Submit Code", cls="button submit-problem")
        ])
    ))


@logged_in_required
def listProblems(request):
    if Contest.getCurrent():
        contest = Contest.getCurrent()
        probCards = []
        for prob in contest.problems:
            probCards.append(Card(
                prob.title,
                prob.description,
                f"/problems/{prob.id}"
            ))
        return HttpResponse(Page(
            h2("Problems", cls="page-title"),
            *probCards
        ))
    elif Contest.getFuture():
        contest = Contest.getFuture()
        return HttpResponse(Page(
            h1("&nbsp;"),
            h1("Contest Starts in", cls="center"),
            h1(contest.start, cls="countdown jumbotron center")
        ))
    elif Contest.getPast():
        return HttpResponse(Page(
            h1("&nbsp;"),
            h1("Contest is Over", cls="center")
        ))
    return HttpResponse(Page(
        h1("&nbsp;"),
        h1("No Contest Created", cls="center")
    ))
