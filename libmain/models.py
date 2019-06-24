from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
def gen_slug(clss,title):
    orig_slug = slugify(title,allow_unicode= True)
    uniq_slug = orig_slug
    n = 1
    while clss.objects.filter(slug=uniq_slug).exists():
        uniq_slug = '{}-{}'.format(uniq_slug,n)
        n += 1
    return uniq_slug


class Book(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100,unique = True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank = True,null=True)
    author = models.CharField(max_length=100,blank = True)
    date =  models.CharField(max_length=100,blank = True)

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = gen_slug(Book,self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
