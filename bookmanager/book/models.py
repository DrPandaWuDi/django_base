from django.db import models

# Create your models here.

# 书籍类
class BookInfo(models.Model):
    name=models.CharField(max_length=10)

    """将模型类以字符串的方式输出"""
    def __str__(self):
        return self.name

# 人物类
class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    # 外键约束
    # TypeError: __init__() missing 1 required positional argument: 'on_delete' 必须设置on_delete
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    """将模型类以字符串的方式输出"""
    def __str__(self):
        return self.name