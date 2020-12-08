from django.shortcuts import render
from .models import Pizza
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PizzaSerializer


# Create your views here.

def index(request):
    data = Pizza.objects.all()
    return render(request, "pizza/index.html", {'data': data})

class pizzaList(APIView):

    def get(self, request):
        piz = Pizza.objects.all()
        serializer = PizzaSerializer(piz,many=True)
        return Response(serializer.data)
        
class pizzaCreate(APIView):

    def get(self, request):
        piz = Pizza.objects.all()
        serializer = PizzaSerializer(piz,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer . is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class pizzaAlter(APIView):

    def get(self, request, pid):
        try:
            piz = Pizza.objects.get(id = pid)
        except Pizza.DoesNotExist:
            return Response('User with id '+pid+' is not found in database', status= status.HTTP_404_NOT_FOUND)
        serializer = PizzaSerializer(piz)
        return Response(serializer.data)

    def delete(self, request, pid):
        piz = Pizza.objects.get(id = pid)
        piz.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

    def put(self, request, pid):
        try:
            piz = Pizza.objects.get(id = pid)
        except Pizza.DoesNotExist:
            return Response('User with id '+pid+' is not found in database', status= status.HTTP_404_NOT_FOUND)
        serializer = PizzaSerializer(piz, data=request.data)
        if serializer . is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
