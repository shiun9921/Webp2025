#from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging

from .models import Post

logger = logging.getLogger('django')

# class HelloApiView(APIView):
#     def get(self, request):
#         my_name = request.GET.get('name' , None)
#         if my_name:
#             retValue ={}
#             retValue['data'] = "Hello" + my_name
#             return JsonResponse (retValue, status=status.HTTP_200_OK)
#         else:
#             return JsonResponse(
#                 {"res": "Parameter: name is None"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
@api_view(['GET'])
def add_post(request):
    id = request.GET.get('id' , '')
    org = request.GET.get('開課單位' , '')
    title = request.GET.get('課程名稱' , '')
    teacher = request.GET.get('授課老師' , '')
    location = request.GET.get('location' , '')
    created_at = request.GET.get('created_at', '')

    new_post = Post()
    new_post.content = org
    new_post.title = title
    new_post.photo = teacher
    new_post.location = location
    new_post.save()
    logger.debug(" ************** myhello_api :" + title)
    if title:
        return JsonResponse({"data": title + " insert!"}, status=status.HTTP_200_OK)
    else:
        return JsonResponse(
            {"res": "parameter: name is None"},
            status=status.HTTP_400_BAD_REQUEST            
        )
    
@api_view(['GET'])
def list_post(request):
    posts = Post.objects.all().values()
    return JsonResponse(list(posts), safe=False)
    # return Response({"data":
    #                  json.dumps(
    #                      list(posts),
    #                      sort_keys = True,
    #                      indent = 1,
    #                      cls = DjangoJSONEncoder)},
    #                 status=status.HTTP_200_OK)
# Create your views here.
# def myIndex(request):
#    my_name = request.GET.get('name', "CGU")
#    return HttpResponse("Hello " + my_name)
