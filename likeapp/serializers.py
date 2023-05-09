from .models import Member
from rest_framework import serializers

# serialze / deserialize 되어야하는 모델의 필드들을 정의해보자.
# 대응하는 모델 내 모든 필드들을 정의해도 되고, 일부 필드만 정의해도 된다.


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

# Q5.
# model에 존재하는 모든 필드를 사용하되,
# 위와는 다르게 필드 명을 직접 명시하고싶다면 
# serializer에서 어떻게 작성하면 될까요?
_________________________________________________________________________________________
# Q6.
# 같은 model을 사용하되,
# 이름, 나이만 입력받아서 사용하는 경우에는
# serializer에서는 어떻게 처리해주어야 할까요?
_________________________________________________________________________________________
# Q7.
# school 필드만 읽기 전용으로 지정하고 싶다면
# serializer에서 어떻게 처리할 수 있을까요?


