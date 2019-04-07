from django.http import HttpResponse
from django.shortcuts import render

from contest import auth, register
from contest.UIElements.lib.htmllib import div, h2, h
from contest.UIElements.lib.page import Page
from contest.register import setHeader


def root(params, setHeader, user):
    setHeader("Location", "/problems")
    return 302


# TODO: start with this view
def login(request, **params):
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
        username = params.get('username')
        password = params.get('password')
        user = auth.checkPassword(username, password)
        if user:
            setHeader("Set-Cookie", f"user={user.id}")
            setHeader("Set-Cookie", f"userType={user.type}")
            return "ok"
        else:
            return "Incorrect username / password"


def logout(params, setHeader, user):
    setHeader("Location", "/login")
    setHeader("Set-Cookie", "user=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT;")
    setHeader("Set-Cookie", "userType=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT")
    return 302


# TODO: move to urls
register.get("/", "loggedin", root)
# register.post("/login", "any", login)
register.get("/logout", "any", logout)
