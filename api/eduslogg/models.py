from django import forms
from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor

class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name

class CareerCategory(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name


class CareerOption(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(CareerCategory, on_delete=models.CASCADE, null=True)
    total_levels = models.IntegerField()

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name

class Institute(models.Model):
    name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True)
    location = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    models.DateField(auto_now=True, auto_now_add=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def profileURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
    



class Blog(models.Model):
    heading = models.CharField(max_length=100, null=True)
    snap = models.ImageField(null=True)
    content = models.CharField(max_length=1000, null=True)

    
    def __repr__(self):
        return self.heading

    def __str__(self):
        return self.heading

    @property
    def snapURL(self):
        try:
            url = self.snap.url
        except:
                url=" "
        return url


class Query(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  query = models.CharField(max_length=500)
      
  def __str__(self):
    return self.query



class CourseCategory(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    course_category = models.ForeignKey(CourseCategory, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name