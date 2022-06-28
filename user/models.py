from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('유저네임은 필수입니다.')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    password = models.CharField("비밀번호", max_length=200)
    fullname = models.CharField("이름", max_length=20)
    email = models.EmailField("이메일", unique=True)
    phone = models.CharField("전화번호", max_length=30)
    join_date = models.DateTimeField("가입일", auto_now_add=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FILED = 'nickname'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f'{self.username} / {self.email}'

