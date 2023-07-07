from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def endpoind(request):
    data = ['/advocate','advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    data = ['shahin','sndeep','shammas']
    return Response(data)

@api_view(['GET'])
def advocate_details(request,username):
    data = username
    return Response(data)