from django.db import models

class Member(models.Model):
    # member_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,blank=False)
    school=models.CharField(max_length=30,blank=False)
    age=models.IntegerField(blank=False)


_________________________________________________________________________________________
# Q8.
# 위와 같이 primary key를 지정하지 않으면 자동으로 pk 할당이 됩니다.
# 그럼 primary key를 직접 입력받아서 사용하는 경우에는
# model에서 어떻게 작성해주어야할까요?

# 공식 문서에서 다양한 필드의 형태를 살펴봅시다!





