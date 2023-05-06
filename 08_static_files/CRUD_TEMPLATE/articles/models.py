from django.db import models

def articles_image_path(instance, filename):
    return f'user_{instance.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # images = models.ImageField(blank=True, upload_to='images/')
    # 주의사항 : 문자열 기반 필드에는 null=True 를 사용하지 않는 것이 좋다.
    # blank 는 validation 단계에서 적용되고
    # null 은 DB 에서 적용되는데
    # 문자열 필드일 경우 둘 다 데이터 없음으로 처리되며
    # django 는 이것을 '데이터 없음'의 상태를 표현하는 '중복'된 방법으로 본다.
    
    # image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/', max_length=500)
    
    image = models.ImageField(blank=True, upload_to=articles_image_path, max_length=500)
    
    

    def __str__(self):
        return self.title
