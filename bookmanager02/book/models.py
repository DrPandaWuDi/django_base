from django.db import models

# Create your models here.
"""
1.模型类，需要继承自models.Model
2.定义属性
    id 系统会默认生成
    属性名=models.类型（选项）
    
    2.1 属性名 对应的就是 字段名
        不要使用 Python MySQL 的关键字
        不要使用连续的下划线（__）
    2.2 类型 ~ MySQL类型
    2.3 选项 是否有默认值，是否唯一，是否为NULL,类似如下
        CharField 必须设置 max_length=
        ForeignKey 必须设置 on_delete=
        verbose_name 主要是 admin站点 使用
    create table "user"{
        id int,
        name varchar(10) not null default ''
    }
3. 改变表的名称
    默认表的名字：子应用名_类名 都是小写
    使用 class Meta 修改
"""


# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=20, unique=True, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 改变表的名字
    class Meta:
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
