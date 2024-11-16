from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='task')    # 사용자
    title = models.CharField(max_length=255)                                        # 제목
    description = models.TextField(blank=True)                                      # 설명
    completed = models.BooleanField(default=False)                                  # 완료 체크
    created_at = models.DateTimeField(auto_now_add=True)                            # 생성일
    updated_at = models.DateTimeField(auto_now=True)                                # 수정일
    
    def __str__(self):
        return self.title