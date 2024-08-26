from django.shortcuts import render
from uuid import uuid4
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view

class GetTokenApiView(APIView):
  def get(self, request):
    rand_token = uuid4()
    token = Token.objects.create(token=rand_token)
    serializer = SerializeToken(token)
    return Response(serializer.data)
    
@api_view(['GET'])
def list_goods(request):
    token = request.GET.get('token')
    if not token:
        return HttpResponse("Token must be present", status=401)
    if not Token.objects.filter(token=token).exists():
        return HttpResponse("Token is invalid", status=401)

    goods = Good.objects.all()
    serializer = SerializeGoods(goods, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def new_good(request):
    token = request.GET.get('token')
    if not token:
        return HttpResponse("Token must be present", status=401)
    if not Token.objects.filter(token=token).exists():
        return HttpResponse("Token is invalid", status=401)

    serializer = SerializeGoods(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
