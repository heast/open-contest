from contest import register
from contest.auth import generatePassword
from contest.models.user import User


def createUser(params, setHeader, user):
    newPassword = generatePassword()
    user = User(
        params["username"],
        newPassword,
        params["type"]
    )
    user.save()
    return newPassword


def deleteUser(params, setHeader, user):
    username = params["username"]
    user = User.getByName(username)
    user.delete()
    return "ok"


# TODO: move to urls
register.post("/createUser", "admin", createUser)
register.post("/deleteUser", "admin", deleteUser)
