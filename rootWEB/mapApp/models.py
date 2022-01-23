from django.db import models

# Create your models here.

class WwgUser(models.Model) :
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_birthyear = models.CharField(max_length=50)

    def __str__(self) :
        return self.user_id

class WwgZerowaste(models.Model) :
    # id
    index = models.IntegerField()
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    about = models.TextField()
    imgURL = models.CharField(max_length=1000)
    img = models.CharField(max_length=300)
    lat = models.FloatField()
    lng = models.FloatField()
    rating = models.FloatField(null = True)
    review1 = models.FloatField(null = True)
    review2 = models.FloatField(null = True)
    WWGScore = models.FloatField(null = True)
    Recomm= models.CharField(max_length=1000,null = True)

    def __str__(self) :
        return self.name

class WwgVegan(models.Model) :
    # id
    index = models.IntegerField()
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    about = models.TextField()
    imgURL = models.CharField(max_length=1000)
    img = models.CharField(max_length=300)
    lat = models.FloatField()
    lng = models.FloatField()
    rating = models.FloatField(null=True)
    review1 = models.FloatField(null=True)
    review2 = models.FloatField(null=True)
    WWGScore = models.FloatField(null=True)
    Recomm = models.CharField(max_length=1000, null=True)

    def __str__(self) :
        return self.name

class TopPlace(models.Model):
    TopVegan = models.CharField(max_length=5000)
    TopZerowaste = models.CharField(max_length=5000)
    Date = models.CharField(max_length=50)

    def __str__(self):
        return self.Date


class VeganClick(models.Model):
    user_id = models.CharField(max_length=50)
    name_index = models.IntegerField()
    name = models.CharField(max_length=200)
    WWGScore = models.FloatField()
    cnt = models.IntegerField()

    def __str__(self):
        return self.user_id + self.name + self.cnt


class ZerowasteClick(models.Model):
    user_id = models.CharField(max_length=50)
    name_index = models.IntegerField()
    name = models.CharField(max_length=200)
    WWGScore = models.FloatField()
    cnt = models.IntegerField()

    def __str__(self):
        return self.user_id + self.name + self.cnt


class WwgUserRecomm(models.Model):
    user_id = models.CharField(max_length=50)
    vegan_recomm = models.CharField(max_length=5000)
    zerowaste_recomm = models.CharField(max_length=5000)

    def __str__(self):
        return self.user_id
