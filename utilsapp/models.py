from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserInfo(AbstractUser):
    """
    重写用户表
    """
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True, null=True)
    email = models.EmailField(verbose_name="用户邮箱", max_length=64, unique=True, null=True)
    lastloginIP = models.CharField(verbose_name="最后登录IP", max_length=32, blank=True)
    lastloginTime = models.DateTimeField(verbose_name="最后登录时间", auto_now=True)
    role_list = ((0, '无角色'), (1, '系统管理员'))
    role = models.SmallIntegerField(choices=role_list, default=0, null=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    @classmethod
    def check_role(self, username):
        return UserInfo.objects.filter(username=username).first().role

    @classmethod
    def user_info(self):
        """ 查询所有用户信息"""
        userinfo = UserInfo.objects.all()
        user_list = [user.username for user in userinfo]
        return user_list
