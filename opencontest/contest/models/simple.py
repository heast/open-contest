import json
import os
import logging
import platform
import shutil

from opencontest.settings import BASE_DIR


def ensureExists(file: str, isDir: bool = False):
    if platform.system() == 'Linux':
        cur = "/"
        for part in file.split("/")[:-1]:
            if part == "":
                continue
            cur += part + "/"
            if not os.path.isdir(cur):
                os.mkdir(cur)
    else:
        path: str = '\\'.join(file.split('\\')[:-1])
        if not os.path.isdir(path):
            os.mkdir(path)


def getKey(key: str) -> dict:
    try:
        # FIXME - windows & linux friendly...
        # with open(BASE_DIR + "\\db\\" + key[1:], "r") as f:
        with open(BASE_DIR + "\\db" + '\\'.join(key.split('/')), "r") as f:
        # with open(/db" + key, "r") as f:
            s = f.read()
            if s[0] in ("[", "{"):
                return json.loads(s)
            return s
    except Exception as e:
        print(e)
        return None


def setKey(key: str, value):
    # TODO: don't forget to put linux-style paths back the way they were.
    # ensureExists("/db" + key)
    ensureExists(BASE_DIR + "\\db" + '\\'.join(key.split('/')))
    # with open("/db" + key, "w") as f:
    with open(BASE_DIR + "\\db" + '\\'.join(key.split('/')), "w") as f:
        if isinstance(value, dict) or isinstance(value, list):
            f.write(json.dumps(value))
        else:
            f.write(value)


def listSubKeys(key: str) -> list:
    # ensureExists("/db" + key + "/file.json")
    ensureExists(BASE_DIR + "\\db" '\\'.join(key.split('/')) + "\\file.json")
    # return [x for x in os.listdir("/db" + key) if not x.startswith(".")]
    # return [x for x in os.listdir("\\db" '\\'.join(key.split('/'))) if not x.startswith(".")]
    return [x for x in os.listdir(BASE_DIR + "\\db" '\\'.join(key.split('/'))) if not x.startswith(".")]



def deleteKey(key: str):
    # shutil.rmtree("/db" + key, ignore_errors=True)
    shutil.rmtree(BASE_DIR + "\\db" + '\\'.join(key.split('/')), ignore_errors=True)
