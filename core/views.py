import json
from django.shortcuts import render


from json import JSONDecodeError
from django.http import HttpResponse, JsonResponse
from .serializers import ContactSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .models import Contact
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
class ContactAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    serializer_class = ContactSerializer

    # Import the channel layer
  
    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def put(self, request):
        try:
            d= Contact.objects.last()
            data = JSONParser().parse(request)
            serializer = ContactSerializer(d,data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
    def get(self, request):
        users = Contact.objects.all()
        serializer = ContactSerializer(users,many=True)
        return Response(serializer.data)
