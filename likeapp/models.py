from django.db import models

class Member(models.Model):
    # member_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,blank=False)
    school=models.CharField(max_length=30,blank=False)
    age=models.IntegerField(blank=False)


