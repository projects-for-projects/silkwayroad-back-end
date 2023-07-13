from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializers import *
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@permission_classes([])
class UserView(APIView):

    serializer_class = UserSerializer

    def get(self, request):
        output = [{"email": output.email, "first_name": output.first_name,"last_name": output.last_name,}
                  for output in UserAccount.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)