from django import forms
from .models import Posts

# 게시글 등록 폼
class PostCreateForm(forms.ModelForm):
    title = forms.CharField(required=False)
    content = forms.CharField(required=False)
    
    class Meta:
        model = Posts
        fields = ['title', 'content']
        
    # 제목 검증
    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError("제목을 입력해주세요.")
        if len(title) < 2:
            raise forms.ValidationError("제목은 최소 2자 이상 입력해주세요.")
        if len(title) > 100:
            raise forms.ValidationError("제목은 최대 100자 이하로 입력해주세요.")
        return title
    
    # 내용 검증
    def clean_content(self):
        content = self.cleaned_data['content']
        if not content:
            raise forms.ValidationError("내용을 입력해주세요.")
        return content

# 게시글 수정 폼
class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(required=False)
    content = forms.CharField(required=False)
    
    class Meta:
        model = Posts
        fields = ['title', 'content']
        
    # 제목 검증
    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError("제목을 입력해주세요.")
        if len(title) < 2:
            raise forms.ValidationError("제목은 최소 2자 이상 입력해주세요.")
        if len(title) > 100:
            raise forms.ValidationError("제목은 최대 100자 이하로 입력해주세요.")
        return title
    
    # 내용 검증
    def clean_content(self):
        content = self.cleaned_data['content']
        if not content:
            raise forms.ValidationError("내용을 입력해주세요.")
        return content
