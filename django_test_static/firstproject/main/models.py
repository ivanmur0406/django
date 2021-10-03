from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField("заголовок",max_length=20)
    text=models.TextField("текст")
    date=models.DateTimeField("дата")