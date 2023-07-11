from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.db.models import Q
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from . models import Advocate,Company
from . serializers import AdvocateSerializer,CompanySerializer


# Create your views here.

@api_view(['GET'])
def endpoind(request):
    data = ['/advocate','advocates/:username']
    return Response(data)



@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def advocate_list(request):
    # data = ['shahin','sndeep','shammas']
    #handles GET requests
        if request.method == 'GET':
            query = request.GET.get('query')

            if query == None:
               query = ''

            advocate = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
            serializer = AdvocateSerializer(advocate,many=True)
            return Response(serializer.data)


        if request.method == 'POST':
            advocate = Advocate.objects.create(
                username = request.data['username'],
                bio = request.data['bio']
        )
        
            serializer = AdvocateSerializer(advocate, many=False)      
            return Response(serializer.data)
        


class AdvocateDetails(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse('Advocate doesent exist')


    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
        
    def put(self, request, username):
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio =request.data['bio']
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('user was deleted')


@api_view(['GET'])
def company_list(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company,many=True)
    return Response(serializer.data)


# @api_view(['GET','PUT','DELETE'])
# def advocate_details(request,username):
#     advocate = Advocate.objects.get(username__icontains=username)

#     if request.method == "GET":
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
#     if request.method == "PUT":
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()

#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == "DELETE":
#         advocate.delete()
#         return Response('user was deleted')