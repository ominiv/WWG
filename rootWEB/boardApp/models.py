from django.db import models

# Create your models here.
class Board(models.Model):
    mainphoto = models.ImageField(blank=True, upload_to="mainphoto", null=True)
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)
    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname

class Board2(models.Model):
    mainphoto = models.ImageField(blank=True, upload_to="mainphoto", null=True)
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)
    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname