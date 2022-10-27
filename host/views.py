
from django.http import JsonResponse



def echo(request):
    res =  { "slackUsername": "String", "backend": "Boolean", "age": "Integer", "bio": "String" }
    return JsonResponse(res)