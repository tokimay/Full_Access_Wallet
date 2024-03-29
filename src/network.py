import requests
from src.validators import checkURI
from src.values import *


def getRequest(uri: str):
    try:
        checkURI(uri)
        result = requests.get(uri)
        return result
    except Exception as er:
        raise Exception(f"getRequest -> {er}")


def getTokenList() -> dict:
    try:
        tokes = {"list": []}
        tokenJson = getRequest(TOKEN_LIST_URI)
        for token in tokenJson.json()['list']:
            tokes['list'].append(token)
        return tokes
    except Exception as er:
        raise Exception(f"addTokensList -> {er}")

