from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('张wu',max_length=30,null=True)
    age = models.IntegerField(null=True)
    pp = models.IntegerField(null=True)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __unicode__(self): #def __unicode_
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name