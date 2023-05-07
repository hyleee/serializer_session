from django.db import models

class Member(models.Model):
    # member_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,blank=False)
    school=models.CharField(max_length=30,blank=False)
    age=models.IntegerField(blank=False)



# 생각해보기
# primary key를 직접 입력받아서 사용하는 경우에는
# model에서 어떻게 작성해주어야할까요?