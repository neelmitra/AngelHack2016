from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Tab
from .serializers import TabSerializer
# Create your views here.


class TabList(viewsets.ModelViewSet):
    serializer_class = TabSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Tab.objects.filter(owner=id)


class TabDetail(viewsets.ModelViewSet):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer