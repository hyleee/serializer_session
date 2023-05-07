# 🌈 DRF

## ✔️ Django REST Framework

> 내가 가진 데이터 또는 기능을 외부에 제공하기 위한 인터페이스 구축

1. 사용자 요청을 받는다.
2. 요청한 정보를 DB에서 꺼내거나 가공한다.
3. 정보를 사용자에게 특정 포맷 (json/xml/txt) 으로 건네준다.

---

## ✔️ REST(Representational State Transfer)

> URI로 표시한 자원에 대한 상태 정보를 행위를 통해 주고받는다.

1. 자원(Resource): URI
2. 행위(Verb): HTTP Method(GET/PSOT/PUT/DELETE 등)

---

## ✔️ API Server

> 프로그래밍을 통해 요청에 따른 JSON을 응답하는 서버

---

## ✔️ JSON (JavaScript Object Notation)

> JavaScript Object 자료 구조의 표현법을 따른 경량형 문자열 교환 포맷.

> 쉽게 말해 key 값과 value 값으로 구성된 흔히 통용되는 데이터 교환 형식!

---

## ✔️ RESTful API, 왜 써야할까?

- 내 DB에 없을 때
- 기능을 직접 구현하지않고 가져다 쓸 때
- 내가 갖고 있는 데이터와 기능을 제공할 때
- 웹 개발 시 SERVER - CLIENT 간 소통을 구현할 때

---

## ✔️ DRF 설치

```
> pip install djangorestframework
```

---

# 🌈 Serializer

> Back-End 에서 열심히 개발한 데이터! Front-End 에게 어떻게 넘겨줄까?

✔️ 직렬화

✔️ django 내부 로직에 따른 복잡한 데이터 -> 다른 framework에서도 이해할 수 있도록 변환된 데이터

✔️ query_set / model instance -> json

---

## 🔥 용어 정의

models.py -> DB 구축
DB -> serializer 사용 -> json
json-> deserializer -> DB

✔️ 직렬화(serialization): 객체를 문자열 또는 바이트로 변환하여 데이터를 전송하는 과정
✔️ 역직렬화(Deserialization): 수신한 바이트를 다시 객체로 변환(메모리 상의 복원)하는 과정

---

## 🔥 Serializer & ModelSerializer

✔️ Django의 Form & ModelForm

```python
# forms.py(ModelForm 사용시)
from django.forms import ModelForm
from .models import Post
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
```

✔️ Serializer & ModelSerializer

```python
# serializers.py(ModelSerializer 사용 시)
from rest_framework.serializers import ModelSerializer
from .models import Post
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
```

✔️ 공통점

- 필드 지정
- 입력된 데이터에 대한 유효성 검사를 진행

✔️ 차이점

- Form 과 ModelForm은 form 태그가 포함된 HTML을 생성
- Serializer와 ModelSerializer는 form 데이터가 포함된 JSON 타입의 문자열을 생성

---

## 🔥 기초 흐름

app 생성 및 urls.py 설정이 완료되어있다고 가정

---

### ✔️ 1.1 DB model 생성

- 모델(=내가 반복해서 사용할 기본 틀)을 만들어보자!
- (참고) 장고에서 모델을 정의할 때 Primary Key로 명시한 필드가 없다면 자동으로 Primary Key로서 id 필드가 정의되고, 데이터 베이스에 모델 인스턴스가 저장될 때마다 id 필드 값은 1씩 증가됨

```python
from django.db import models

class Member(models.Model):
    # member_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,blank=False)
    school=models.CharField(max_length=30,blank=False)
    age=models.IntegerField(blank=False)
```

---

### ✔️ 1.2 DB Migration

```
> python manage.py makemigrations
> python manage.py migrate
```

---

### ✔️ 2. Serializer 생성

- 내가 클라이언트에게 보낼 데이터를 serializer에 삽입하여 변환시켜보자!
- 특정 모델에 대응하는 시리얼라이저를 정의
- 일반적으로 Class명은 Model 명 + Serializer
- 본 예시에서는 create(), update() 메소드를 기본으로 제공해주는 ModelSerializer를 상속받아 사용해보았습니다:)

```python
from .models import Member
from rest_framework import serializers

# serialze / deserialize 되어야하는 모델의 필드들을 정의해보자.
# 외부로 공개해도 괜찮은 필드들만 선언
# 대응하는 모델 내 모든 필드들을 정의해도 되고, 일부 필드만 정의해도 된다.


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
```

---

### ✔️ 3. Serializer를 사용한 views.py 작성

- serializer가 예쁘게 변환해준 데이터를 views.py를 통해 가져와보자!
- serialzers.py 에서 만든 serializer와 models.py에서 만든 model을 import
- 본 예시에서는 FBV(Function Based View)와 CBV(Class Based View) 2가지 방법 중 CBV 를 사용해보았습니다:)

```python
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
```

---

### ✔️ 4. json 형태가 잘 반환되는지 확인해볼까요?

- postman 은 다음 세션 때 활용해볼 예정이니 지금은 데이터 결과에 집중해주세요!( •̀ ω •́ )✧

![](https://velog.velcdn.com/images/cutehypretty/post/b7ec2541-2f13-4cff-9c83-8c369ec935a9/image.png)
[사진1] 초기 상태. GET 요청해도 빈 데이터 목록 반환

![](https://velog.velcdn.com/images/cutehypretty/post/424b186d-6eaa-4a52-be16-651063189586/image.png)
[사진2] POST 로 멤버 추가

![](https://velog.velcdn.com/images/cutehypretty/post/5dbf554a-b207-40c5-b89c-fac3956653de/image.png)
[사진3] GET 요청 시 POST 한 멤버 목록 조회

![](https://velog.velcdn.com/images/cutehypretty/post/a462e981-a2ab-4943-80de-ef05c601c626/image.png)
[사진4] PUT 요청으로 나이를 수정해서 한 살 젊어져보자!

---

## 🔥 (참고) DRF 에서 제공해주는 찐 기본 Serializer를 사용한다면?

(사용 권장 X 원리이해 용도 O)

✔️ 단순 Serializer를 사용한다면 다양한 메소드가 포함된 타 Serializer와는 다르게 create(), update() 메소드 등을 직접 정의해주어야합니다! ~~귀찮죠..?~~

✔️ cretae() 메소드는 serializer를 대상으로 save() 메소드를 호출하여 DB의 인스턴스를 생성하고자 할 때의 동작을 정의

✔️ update() 메소드는 serializer를 대상으로 save() 메소드를 호출함으로써 DB 인스턴스를 수정하고자 할 때의 동작을 정의

```python
class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=30)
    school = serializers.CharField(required=True, max_length=30)
    age = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.school = validated_data.get('school', instance.school)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
```

---

## 참고 문헌

https://www.django-rest-framework.org/api-guide/serializers/#serializers

```

```
