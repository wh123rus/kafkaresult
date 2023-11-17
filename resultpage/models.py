from django.db import models
import os

# Create your models here.

class Menu(models.Model):
    pod_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    number = models.IntegerField()
    uuid = models.CharField(max_length=255, unique=True, primary_key = True)

    def __str__(self):
        return self.uuid  # 모델을 출력할 때 보여질 필드 선택
    class Meta:
        # 기존 테이블 이름 지정
        db_table = os.getenv('DB_TABLE', 'testmenu')