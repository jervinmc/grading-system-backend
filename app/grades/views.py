from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Grades
from .serializers import GradesSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class GradesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Grades.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=GradesSerializer



class GradesBySubject(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        print(res)
        print("okay")
        item = Grades.objects.filter(user_id ='1',subject_id = res.get('subject_id'))
        item = GradesSerializer(item,many=True)
        # for x in item.data:
        #     s_item = Subject.objects.filter(id=x['subject_id'])
        #     s_item = SubjectSerializer(s_item,many=True)
        #     if(len(s_item.data)!=0):
        #         x['subject_name'] = s_item.data[0]['subject_name']
        print(item.data)
        return Response(status=status.HTTP_200_OK,data=item.data)


class GradesBySubjectAll(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        print(res)
        u_item = User.objects.all()
        u_item = GetUserSerializer(u_item,many=True)
        total_activity = 0
        total_exam = 0
        counter = 1
        for x in u_item.data:
            item = Grades.objects.filter(subject_id = res.get('subject_id'),user_id=x['id'])
            item = GradesSerializer(item,many=True)
            for i in item.data:
                if(i['grade_type']=='Activity'):
                    total_activity = total_activity + i['score']
                    counter = counter + 1
            x['total_activity'] = total_activity/counter
            counter = 1
            total_activity = 0
            for i in item.data:
                if(i['grade_type']=='Exam'):
                    total_exam = total_exam + i['score']
                    counter = counter + 1
            x['total_exam'] = total_exam/counter
            counter = 1
            total_activity = 0

        
        print(u_item.data)
        # for x in item.data:
        #     s_item = Subject.objects.filter(id=x['subject_id'])
        #     s_item = SubjectSerializer(s_item,many=True)
        #     if(len(s_item.data)!=0):
        #         x['subject_name'] = s_item.data[0]['subject_name']
        # print(item.data)
        return Response(status=status.HTTP_200_OK,data=u_item.data)