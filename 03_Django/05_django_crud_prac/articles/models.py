from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f'제목:{self.title}, 내용:{self.content}'