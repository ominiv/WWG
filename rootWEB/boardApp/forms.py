from django import forms
from .models import Writing  # 폼을 적용할 모델을 불러온다.
from django.forms import ModelForm
from .models import FileUpload


class WritingForm(forms.ModelForm):
    class Meta:
        model = Writing  # 사용할 모델
        fields = ['subject', 'content']  # 폼으로 입력할 필드를 입력해준다.
        # fields에 '__all__'을 따옴표까지 함께 넣어주면 모든 필드를 가져오라는 명령이 된다.

class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'imgfile', 'content']