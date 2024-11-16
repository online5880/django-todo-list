from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        labels = {
            'title': '제목',
            'description': '내용',
            'completed': '완료 여부'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '할 일의 제목을 입력하세요'}),
            'description': forms.Textarea(attrs={'placeholder': '할 일의 내용을 입력하세요'}),
        }