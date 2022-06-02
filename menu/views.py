from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import MenuSerializer
from django.http.response import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .models import Menu
from rest_framework.filters import SearchFilter
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class searchMenu(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [SearchFilter]

    search_fields = ['category','plate_size','discount','price','item_name']


@csrf_exempt
def addItem(request):
    if request.method == "POST":
        items = request.body
        itemStream = io.BytesIO(items)
        dataItems = JSONParser().parse(itemStream)
        serializedData = MenuSerializer(data=dataItems)
        if serializedData.is_valid():
            serializedData.save()
            responseMessage={'message':"Items added successfully"}
            return JsonResponse(responseMessage)
        json_data=JSONRenderer().render(serializedData.error)
        return HttpResponse(json_data,content_type='application/json')

def viewMenu(request):
    if request.method == "GET":
        allItems = Menu.objects.all()
        serializedItems = MenuSerializer(allItems,many=True)
        return JsonResponse(serializedItems.data,safe=False)
