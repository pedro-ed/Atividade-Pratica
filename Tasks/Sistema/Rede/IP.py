import requests

def GetMyIP():
    return requests.get("https://api4.my-ip.io/ip").text

