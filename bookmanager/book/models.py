from django.db import models

# Create your models here.

# 书籍类
class BookInfo(models.Model):
    name=models.CharField(max_length=10)

# 人物类
class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    # 外键约束
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)