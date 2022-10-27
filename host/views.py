
from django.http import JsonResponse

username="usman"
age=21
bio="A Backend engineer ."

def echo(request):
    res =  { "slackUsername": username, "backend": True, "age": age, "bio": bio }
    return JsonResponse(res)
