from django.shortcuts import render 
from django.http import request 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from nrmlapi.serializer import CompanySerializer
from .models import Company
# from rest_framework.renderers import JSONRenderer
# Create your views here.

@api_view(['GET', 'POST', 'PATCH'])
# @renderer_classes([JSONRenderer])
def home(request):
    if request.method == 'GET':
        return Response({
            'status' : '200',
            'Message': 'success message',
            'message_called' : 'you callet GET Method',
        })
        
    elif request.method == 'POST':
        return Response({
            'status' : '300',
            'Message': 'success message',
            'message_called' : 'you callet POST Method',
        })
    
    elif request.method == 'PATCH':
        return Response({
            'status' : '400',
            'Message': 'success message',
            'message_called' : 'you callet PATCH Method',
        }) 
    else :
        return 'you are checking wrong method 500 error'
    
@api_view(['GET'])
def get_details(request):
    # company_obj = Company.objects.all()   # to get all obj from Company model
    # Serializer = CompanySerializer(company_obj, many=True)  #to serialize that object to json, many=True --> many fields
        data = request.data 
        # print(data)    #printing the value which we are posting 
        Serializer = CompanySerializer(data = data)
    
        return Response(Serializer.initial_data) #get all data in jason format 
    
@api_view(['POST'])
def post_details(request):
    try:
        data = request.data 
        print(data)    #printing the value which we are posting 
        serializer = CompanySerializer(data = data)  #class have data variable in which we are passing requested data 
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response({
                'status' : True,
                'Message': 'success data',
                'data': serializer.data
            })   
        return Response({
                'status' : False,
                'Message': 'Invalid data',
                'data' : serializer.errors
            })  
    except Exception as e:
        print(e)
        
        return Response({
            'status' : False,
            'Message': 'something went wrong',
        })  
    