from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Tab
import hashlib, json
from .serializers import TabSerializer
# Create your views here.


class TabList(viewsets.ModelViewSet):
    serializer_class = TabSerializer

    def get_queryset(self):
        id = self.request.GET['id']
        return Tab.objects.filter(owner=id)


class TabDetail(viewsets.ModelViewSet):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer

class Pin(APIView):
    def get(self, request, login):
        sha = hashlib.sha1(login.encode('utf-8'))
        hexa = sha.hexdigest()
        pin = int(hexa, 16) % 1000000
        return Response({'pin': pin})
