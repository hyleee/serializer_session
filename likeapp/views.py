# 데이터 처리
from .models import Member
from .serializers import MemberSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Member의 목록을 보여주는 역할
class MemberList(APIView):
    # Member list를 보여줄 때
    def get(self, request):
        members = Member.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    # 새로운 Member 정보를 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Member의 detail을 보여주는 역할
class MemberDetail(APIView):
    # Member 객체 가져오기
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404
    
    # Member의 detail 보기
    def get(self, request, pk, format=None):
        Member = self.get_object(pk)
        serializer = MemberSerializer(Member)
        return Response(serializer.data)

    # Member 수정하기
    def put(self, request, pk, format=None):
        Member = self.get_object(pk)
        serializer = MemberSerializer(Member, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Member 삭제하기
    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

# _________________________________________________________________________________________

# 생각해보기 1
# 아래와 같이 class 를 정의해도 동일 기능을 수행할 수 있을까요?

# from rest_framework import generics

# # Member의 목록을 보여주는 역할
# class MemberList(generics.ListCreateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer

# # Member의 detail을 보여주는 역할
# class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer

# _____________________________________________________________________________________________

# 생각해보기 2
# 아래와 같이 class 를 정의해도 동일 기능을 수행할 수 있을까요?

# from rest_framework import viewsets

# # Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer