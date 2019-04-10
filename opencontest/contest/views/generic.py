from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from contest import auth, register
from contest.UIElements.lib.htmllib import div, h2, h
from contest.UIElements.lib.page import Page
from contest.auth import logged_in_required
from contest.register import setHeader


@logged_in_required
def root(params, setHeader, user):
    return redirect(reverse('listProblems'))
    # setHeader("Location", "/problems")
    # return 302


# @csrf_exempt
def login(request):
    if request.method == 'GET':
        return HttpResponse(Page(
        div(cls="login-box", contents=[
            h2("Login", cls="login-header"),
            h.label("Username", cls="form-label"),
            h.input(name="username", cls="form-control"),
            h.label("Password", cls="form-label"),
            h.input(name="password", cls="form-control", type="password"),
            div(cls="align-right", contents=[
                h.button("Login", cls="button login-button")
            ])
        ])
        ))
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.checkPassword(username, password)
        if user:
            resp = JsonResponse('ok', safe=False)
            resp.set_cookie('user', user.id)
            resp.set_cookie('userType', user.type)
            return resp
        else:
            return JsonResponse('Incorrect username / password', safe=False)


def logout(request):
    resp = HttpResponseRedirect('/login')
    resp.set_cookie('user', 'deleted', expires='Thu, 01 Jan 1970 00:00:00 GMT;')
    resp.set_cookie('userType', 'deleted', expires='Thu, 01 Jan 1970 00:00:00 GMT;')
    # setHeader("Location", "/login")
    # setHeader("Set-Cookie", "user=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT;")
    # setHeader("Set-Cookie", "userType=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT")
    return resp
