from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Enrolled
from .serializers import EnrolledSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from subject.models import Subject
from subject.serializers import SubjectSerializer
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class EnrolledView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Enrolled.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=EnrolledSerializer


class EnrolledByUser(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        print(res)
        item = Enrolled.objects.filter(user_id = res.get('user_id'))
        item = EnrolledSerializer(item,many=True)
        print(item.data)
        print("?")
        for x in item.data:
            s_item = Subject.objects.filter(id=x['subject_id'])
            s_item = SubjectSerializer(s_item,many=True)
            if(len(s_item.data)!=0):
                x['subject_name'] = s_item.data[0]['subject_name']
        print(item.data)
        return Response(status=status.HTTP_200_OK,data=item.data)



